import os
import time
import math
import requests
from tiktok_auth import load_token

API_BASE = "https://open.tiktokapis.com/v2"

# Chunk size 10 MB (TikTok max chunk = 64 MB, min = 5 MB)
CHUNK_SIZE = 10 * 1024 * 1024


def _init_upload(access_token, file_size, caption=""):
    url = f"{API_BASE}/post/publish/video/init/"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json; charset=UTF-8",
    }

    total_chunks = math.ceil(file_size / CHUNK_SIZE)

    payload = {
        "post_info": {
            "title": caption,
            "privacy_level": "PUBLIC_TO_EVERYONE",
            "disable_duet": False,
            "disable_comment": False,
            "disable_stitch": False,
        },
        "source_info": {
            "source": "FILE_UPLOAD",
            "video_size": file_size,
            "chunk_size": CHUNK_SIZE,
            "total_chunk_count": total_chunks,
        },
    }

    resp = requests.post(url, json=payload, headers=headers)
    resp.raise_for_status()
    data = resp.json()

    if data.get("error", {}).get("code") != "ok":
        raise Exception("Init upload gagal:", data)

    return data["data"]["publish_id"], data["data"]["upload_url"]


def _upload_chunks(upload_url, file_path, file_size):
    total_chunks = math.ceil(file_size / CHUNK_SIZE)

    with open(file_path, "rb") as f:
        for chunk_idx in range(total_chunks):
            chunk_data = f.read(CHUNK_SIZE)
            start = chunk_idx * CHUNK_SIZE
            end = start + len(chunk_data) - 1

            headers = {
                "Content-Range": f"bytes {start}-{end}/{file_size}",
                "Content-Length": str(len(chunk_data)),
                "Content-Type": "video/mp4",
            }

            resp = requests.put(upload_url, data=chunk_data, headers=headers)
            resp.raise_for_status()

            print(f"  Chunk {chunk_idx + 1}/{total_chunks} terupload")


def _poll_status(access_token, publish_id, max_wait=120):
    url = f"{API_BASE}/post/publish/status/fetch/"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json; charset=UTF-8",
    }

    elapsed = 0
    interval = 5

    while elapsed < max_wait:
        resp = requests.post(url, json={"publish_id": publish_id}, headers=headers)
        resp.raise_for_status()
        data = resp.json()

        status = data.get("data", {}).get("status", "")
        print(f"  Status: {status}")

        if status == "PUBLISH_COMPLETE":
            return True

        if status in ("FAILED", "PUBLISH_FAILED"):
            reason = data.get("data", {}).get("fail_reason", "unknown")
            raise Exception(f"Upload gagal: {reason}")

        time.sleep(interval)
        elapsed += interval

    raise TimeoutError("Upload timeout setelah menunggu lama")


def upload_to_tiktok(file_path, caption=""):
    print(f"\nUpload ke TikTok: {os.path.basename(file_path)}")

    try:
        access_token = load_token()
        file_size = os.path.getsize(file_path)

        if not caption:
            caption = os.path.splitext(os.path.basename(file_path))[0]

        print("  Init upload...")
        publish_id, upload_url = _init_upload(access_token, file_size, caption)

        print("  Upload video...")
        _upload_chunks(upload_url, file_path, file_size)

        print("  Menunggu publish...")
        _poll_status(access_token, publish_id)

        print(f"  Berhasil upload: {os.path.basename(file_path)}")

    except FileNotFoundError as e:
        print(f"  Skipped - {e}")

    except Exception as e:
        print(f"  Upload gagal: {e}")
