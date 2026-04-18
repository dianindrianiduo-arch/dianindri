"""
TikTok OAuth 2.0 - jalankan sekali untuk dapatkan access token.

Cara pakai:
  1. Isi CLIENT_KEY dan CLIENT_SECRET dari https://developers.tiktok.com
  2. Jalankan: python tiktok_auth.py
  3. Buka URL yang muncul di browser, login, izinkan akses
  4. Paste redirect URL ke terminal
  5. Token tersimpan di tiktok_token.json (otomatis di-refresh)
"""

import json
import os
import time
import secrets
import urllib.parse
import webbrowser
import requests

TOKEN_FILE = "tiktok_token.json"

# Isi dari TikTok Developer Portal
CLIENT_KEY = os.getenv("TIKTOK_CLIENT_KEY", "")
CLIENT_SECRET = os.getenv("TIKTOK_CLIENT_SECRET", "")

REDIRECT_URI = "https://localhost/"
SCOPES = "video.publish,video.upload"

AUTH_URL = "https://www.tiktok.com/v2/auth/authorize/"
TOKEN_URL = "https://open.tiktokapis.com/v2/oauth/token/"


def get_auth_url():
    state = secrets.token_urlsafe(16)
    params = {
        "client_key": CLIENT_KEY,
        "scope": SCOPES,
        "response_type": "code",
        "redirect_uri": REDIRECT_URI,
        "state": state,
    }
    return AUTH_URL + "?" + urllib.parse.urlencode(params), state


def exchange_code(code):
    resp = requests.post(TOKEN_URL, data={
        "client_key": CLIENT_KEY,
        "client_secret": CLIENT_SECRET,
        "code": code,
        "grant_type": "authorization_code",
        "redirect_uri": REDIRECT_URI,
    })
    resp.raise_for_status()
    data = resp.json()
    data["expires_at"] = int(time.time()) + data.get("expires_in", 86400)
    with open(TOKEN_FILE, "w") as f:
        json.dump(data, f, indent=2)
    print("Token tersimpan di", TOKEN_FILE)
    return data


def refresh_token(token_data):
    resp = requests.post(TOKEN_URL, data={
        "client_key": CLIENT_KEY,
        "client_secret": CLIENT_SECRET,
        "grant_type": "refresh_token",
        "refresh_token": token_data["refresh_token"],
    })
    resp.raise_for_status()
    data = resp.json()
    data["expires_at"] = int(time.time()) + data.get("expires_in", 86400)
    with open(TOKEN_FILE, "w") as f:
        json.dump(data, f, indent=2)
    return data


def load_token():
    if not os.path.exists(TOKEN_FILE):
        raise FileNotFoundError(
            "tiktok_token.json tidak ditemukan.\n"
            "Jalankan: python tiktok_auth.py"
        )

    with open(TOKEN_FILE) as f:
        data = json.load(f)

    # refresh jika expired (sisa < 5 menit)
    if int(time.time()) >= data["expires_at"] - 300:
        print("Token expired, refresh...")
        data = refresh_token(data)

    return data["access_token"]


if __name__ == "__main__":
    if not CLIENT_KEY or not CLIENT_SECRET:
        print("Set environment variable dulu:")
        print("  export TIKTOK_CLIENT_KEY=xxxx")
        print("  export TIKTOK_CLIENT_SECRET=xxxx")
        exit(1)

    url, state = get_auth_url()

    print("\nBuka URL ini di browser:")
    print(url)
    webbrowser.open(url)

    print("\nSetelah login & approve, browser akan redirect ke localhost (error itu normal).")
    redirect = input("Paste full redirect URL di sini: ").strip()

    parsed = urllib.parse.urlparse(redirect)
    params = urllib.parse.parse_qs(parsed.query)

    code = params.get("code", [None])[0]
    if not code:
        print("Code tidak ditemukan di URL.")
        exit(1)

    token_data = exchange_code(code)
    print("Access token:", token_data["access_token"][:20], "...")
    print("Selesai! Sekarang bisa jalankan main.py")
