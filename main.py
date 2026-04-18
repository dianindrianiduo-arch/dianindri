import os
import random
import string
import time
from yt_dlp import YoutubeDL
from moviepy import VideoFileClip
from tiktok_uploader import upload_to_tiktok


# ================= CONFIG =================

SEARCH_QUERIES = [
    "afgan live concert hd",
    "afgan official performance hd",
    "afgan interview hd",
    "afgan backstage hd",
    "afgan tv performance hd"
]

JUMLAH_VIDEO = 2
CLIP_MIN = 20
CLIP_MAX = 45

COOKIE_FILE = "cookies.txt"

DESKTOP = os.path.join(os.path.expanduser("~"), "Desktop")

INPUT_FOLDER = os.path.join(DESKTOP, "input")
OUTPUT_FOLDER = os.path.join(DESKTOP, "output")
TEMP_FOLDER = os.path.join(DESKTOP, "temp")

# Set True untuk auto-upload setelah render
AUTO_UPLOAD_TIKTOK = True


# ================= PREPARE FOLDER =================

os.makedirs(INPUT_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
os.makedirs(TEMP_FOLDER, exist_ok=True)


# ================= UTIL =================

def random_filename(length=10):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))


# ================= SEARCH YOUTUBE =================

def search_sources():

    print("Scraping YouTube...")

    query = random.choice(SEARCH_QUERIES)

    try:

        ydl_opts = {
            "quiet": True,
            "extract_flat": True,
            "skip_download": True,
            "cookiefile": COOKIE_FILE,
            "extractor_args": {
                "youtube": {
                    "player_client": ["android"]
                }
            }
        }

        with YoutubeDL(ydl_opts) as ydl:

            results = ydl.extract_info(
                f"ytsearch10:{query}",
                download=False
            )

        entries = results.get("entries", [])

        if not entries:
            raise Exception("Search kosong")

        random.shuffle(entries)

        return entries[:JUMLAH_VIDEO]

    except Exception as e:

        print("Search gagal:", e)
        print("Fallback ke video default Afgan")

        return [
            {"id": "QhJzE2mZ9Ww"},
            {"id": "h8xF0vKQItM"}
        ]


# ================= DOWNLOAD =================

def download(video_id):

    file_path = os.path.join(TEMP_FOLDER, f"{video_id}.mp4")

    url = f"https://youtube.com/watch?v={video_id}"

    print("Download:", video_id)

    ydl_opts = {
        "format": "bestvideo[height>=1080]+bestaudio/best",
        "outtmpl": file_path,
        "cookiefile": COOKIE_FILE,
        "sleep_interval": 5,
        "max_sleep_interval": 10,
        "merge_output_format": "mp4",
        "extractor_args": {
            "youtube": {
                "player_client": ["android"]
            }
        }
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return file_path


# ================= SMART PORTRAIT CROP =================

def crop_portrait(video):

    w, h = video.size
    target_ratio = 9 / 16

    if w / h > target_ratio:

        new_w = int(h * target_ratio)
        center = w // 2

        video = video.cropped(
            x1=center - new_w // 2,
            x2=center + new_w // 2
        )

    if video.h >= 1920:
        return video.resized(height=1920)

    return video


# ================= CLIP =================

def make_clip(src):

    video = VideoFileClip(src)

    if video.duration < CLIP_MIN:

        print("Video terlalu pendek:", src)
        return None

    start = random.randint(0, int(video.duration - CLIP_MAX))
    duration = random.randint(CLIP_MIN, CLIP_MAX)

    clip = video.subclipped(start, start + duration)

    clip = crop_portrait(clip)

    filename = random_filename() + ".mp4"

    output_path = os.path.join(OUTPUT_FOLDER, filename)

    print("Render:", filename)

    clip.write_videofile(
        output_path,
        codec="libx264",
        audio_codec="aac",
        bitrate="8000k",
        threads=4
    )

    return output_path


# ================= INPUT LOCAL =================

def get_local_videos():

    videos = []

    for f in os.listdir(INPUT_FOLDER):

        if f.lower().endswith(".mp4"):

            videos.append(os.path.join(INPUT_FOLDER, f))

    random.shuffle(videos)

    return videos[:JUMLAH_VIDEO]


# ================= MAIN =================

def main():

    local_videos = get_local_videos()

    if local_videos:

        print("Menggunakan video dari Desktop/input")

        for vid in local_videos:

            output_path = make_clip(vid)

            if AUTO_UPLOAD_TIKTOK and output_path:
                time.sleep(random.randint(10, 20))
                upload_to_tiktok(output_path)

        print("Selesai → cek Desktop/output")

        return


    print("Folder input kosong → scraping YouTube")

    sources = search_sources()

    for s in sources:

        try:

            time.sleep(random.randint(5, 9))

            src = download(s["id"])

            output_path = make_clip(src)

            if AUTO_UPLOAD_TIKTOK and output_path:
                time.sleep(random.randint(10, 20))
                upload_to_tiktok(output_path)

        except Exception as e:

            print("Error:", e)


    print("Selesai → cek Desktop/output")


# ================= RUN =================

if __name__ == "__main__":

    main()
