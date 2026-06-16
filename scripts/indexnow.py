#!/usr/bin/env python3
"""IndexNow 즉시 색인 통보 — 빙(Bing)·네이버(Naver)·얀덱스 등에 URL 변경을 알린다.

IndexNow는 한 곳(api.indexnow.org)에 통보하면 참여 검색엔진 전체에 전파된다.
구글은 IndexNow에 참여하지 않으므로 google_indexing.py 를 함께 사용한다.

사용법:
  python3 scripts/indexnow.py --all            # sitemap.xml 의 모든 URL 통보
  python3 scripts/indexnow.py --changed        # 직전 커밋 대비 변경된 페이지만 통보
  python3 scripts/indexnow.py URL [URL ...]     # 특정 URL 직접 통보

키 파일은 빌드 시 루트에 <INDEXNOW_KEY>.txt 로 게시된다(build.py).
"""
import argparse
import json
import os
import re
import subprocess
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from content.site import BASE_URL, INDEXNOW_KEY  # noqa: E402

BASE = BASE_URL.rstrip("/")
HOST = re.sub(r"^https?://", "", BASE)
ENDPOINT = "https://api.indexnow.org/indexnow"


def urls_from_sitemap() -> list:
    path = os.path.join(ROOT, "sitemap.xml")
    with open(path, encoding="utf-8") as f:
        return re.findall(r"<loc>(.*?)</loc>", f.read())


def urls_from_changed() -> list:
    """직전 커밋과 비교해 추가/수정된 index.html 을 URL 로 환산한다."""
    try:
        out = subprocess.check_output(
            ["git", "diff", "--name-only", "--diff-filter=ACMR", "HEAD~1", "HEAD"],
            cwd=ROOT, text=True,
        )
    except subprocess.CalledProcessError:
        out = ""
    urls = []
    for line in out.splitlines():
        line = line.strip()
        if not line.endswith("index.html"):
            continue
        rel = line[: -len("index.html")]
        urls.append(BASE + "/" + rel)
    return urls


def submit(urls: list) -> None:
    urls = sorted({u for u in urls if u.startswith(BASE)})
    if not urls:
        print("통보할 URL이 없습니다.")
        return
    payload = {
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": f"{BASE}/{INDEXNOW_KEY}.txt",
        "urlList": urls,
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT, data=data,
        headers={"Content-Type": "application/json; charset=utf-8"},
    )
    print(f"IndexNow → {ENDPOINT}")
    print(f"  host={HOST}  urls={len(urls)}")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            print(f"  응답: HTTP {resp.status} {resp.reason}")
            # 200/202 = 정상 접수
    except urllib.error.HTTPError as e:
        print(f"  HTTP 오류 {e.code}: {e.read().decode('utf-8', 'ignore')[:300]}")
        sys.exit(1)
    except Exception as e:  # noqa: BLE001
        print(f"  전송 실패: {e}")
        sys.exit(1)
    for u in urls:
        print("   •", u)


def main() -> None:
    ap = argparse.ArgumentParser(description="IndexNow 색인 통보")
    ap.add_argument("urls", nargs="*", help="통보할 URL 목록")
    ap.add_argument("--all", action="store_true", help="sitemap.xml 전체 통보")
    ap.add_argument("--changed", action="store_true", help="변경 페이지만 통보")
    args = ap.parse_args()

    if args.all:
        submit(urls_from_sitemap())
    elif args.changed:
        submit(urls_from_changed())
    elif args.urls:
        submit(args.urls)
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
