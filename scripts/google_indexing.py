#!/usr/bin/env python3
"""구글 Indexing API — URL 변경/삭제를 구글에 직접 통보한다(구글은 IndexNow 미참여).

준비물:
  1) Google Cloud 프로젝트에서 "Indexing API" 사용 설정
  2) 서비스 계정 생성 → JSON 키 발급
  3) Search Console 속성에서 그 서비스 계정 이메일을 '소유자'로 추가
  4) 환경변수 GOOGLE_APPLICATION_CREDENTIALS=서비스계정.json (또는 --credentials)

의존성:
  pip install google-auth requests   (scripts/requirements.txt)

사용법:
  python3 scripts/google_indexing.py --all
  python3 scripts/google_indexing.py --changed
  python3 scripts/google_indexing.py URL [URL ...]
  python3 scripts/google_indexing.py --delete URL   # 삭제 통보(URL_DELETED)

주의: Indexing API는 공식적으로 JobPosting·BroadcastEvent 구조화 페이지를 위한
것이며 일반 URL 통보는 보장되지 않습니다. 색인의 정식 경로는 Search Console +
사이트맵이며, 본 스크립트는 발견 가속을 위한 보조 수단입니다. 일일 호출 쿼터(기본
200)도 유의하세요.
"""
import argparse
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from content.site import BASE_URL  # noqa: E402

BASE = BASE_URL.rstrip("/")
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
SCOPES = ["https://www.googleapis.com/auth/indexing"]


def _session(credentials_path: str):
    try:
        from google.oauth2 import service_account
        from google.auth.transport.requests import AuthorizedSession
    except ImportError:
        sys.exit("의존성 누락: pip install -r scripts/requirements.txt")
    creds = service_account.Credentials.from_service_account_file(
        credentials_path, scopes=SCOPES
    )
    return AuthorizedSession(creds)


def urls_from_sitemap() -> list:
    with open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8") as f:
        return re.findall(r"<loc>(.*?)</loc>", f.read())


def urls_from_changed() -> list:
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
        if line.endswith("index.html"):
            urls.append(BASE + "/" + line[: -len("index.html")])
    return urls


def publish(session, urls: list, notify_type: str) -> None:
    urls = sorted({u for u in urls if u.startswith(BASE)})
    if not urls:
        print("통보할 URL이 없습니다.")
        return
    ok = 0
    for u in urls:
        resp = session.post(ENDPOINT, json={"url": u, "type": notify_type})
        status = "OK" if resp.status_code == 200 else f"ERR {resp.status_code}"
        if resp.status_code == 200:
            ok += 1
        print(f"  [{status}] {notify_type}  {u}")
        if resp.status_code != 200:
            print("        ", resp.text[:200])
    print(f"\n완료: {ok}/{len(urls)} 성공")


def main() -> None:
    ap = argparse.ArgumentParser(description="구글 Indexing API 통보")
    ap.add_argument("urls", nargs="*")
    ap.add_argument("--all", action="store_true", help="sitemap.xml 전체")
    ap.add_argument("--changed", action="store_true", help="변경 페이지만")
    ap.add_argument("--delete", action="store_true", help="URL_DELETED 통보")
    ap.add_argument(
        "--credentials",
        default=os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", ""),
        help="서비스 계정 JSON 경로",
    )
    args = ap.parse_args()

    if not args.credentials or not os.path.exists(args.credentials):
        sys.exit("서비스 계정 JSON이 필요합니다. --credentials 또는 "
                 "GOOGLE_APPLICATION_CREDENTIALS 환경변수를 설정하세요.")

    notify_type = "URL_DELETED" if args.delete else "URL_UPDATED"
    session = _session(args.credentials)

    if args.all:
        publish(session, urls_from_sitemap(), notify_type)
    elif args.changed:
        publish(session, urls_from_changed(), notify_type)
    elif args.urls:
        publish(session, args.urls, notify_type)
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
