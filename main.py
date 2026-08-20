import os
import random
import time
import requests

# أجهزة موبايل حقيقية (Android & iOS)
USER_AGENTS = [
    "Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.210 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.80 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/118.0.5993.69 Mobile/15E148 Safari/604.1",
]


def send_visit(visit_num):
    headers = {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept-Language": random.choice(["en-US,en;q=0.9", "en-CA,en;q=0.9"]),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    }
    try:
        url = "https://loveoooouuu.blogspot.com/"
        response = requests.get(url, headers=headers, timeout=15)
        print(f"✅ [Visit {visit_num}] Success - Status Code: {response.status_code}")
    except Exception as e:
        print(f"❌ [Visit {visit_num}] Failed: {e}")


if __name__ == "__main__":
    for i in range(1, 101):
        send_visit(i)
        time.sleep(random.uniform(0.5, 1.5))
