# 사이트 공통 설정
# 배포 도메인 확정 후 BASE_URL 을 실제 도메인으로 변경하세요.
BASE_URL = "https://uijeongbu-massage.pages.dev"

# 네이버 서치어드바이저 사이트 소유확인 메타 태그 값(메인페이지 head에만 삽입).
NAVER_SITE_VERIFICATION = "ebadb8e2af1a339a08289b322a2844f349eba2ce"

# IndexNow 키 — 루트에 <INDEXNOW_KEY>.txt 파일로 게시된다.
# 빙(Bing)·네이버(Naver)·얀덱스 등 IndexNow 참여 검색엔진에 즉시 색인을 통보할 때 사용.
INDEXNOW_KEY = "6e36c313607143fbbb7e63b6555ddec75fe28dfca5024774b365dfb1c9348238"

BRAND = "간다GO"
BRAND_MARK = "GO"
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

# 대표 행정동 10곳 (slug, 한글명) — 내부링크·메뉴 공용
# 번호 행정동(의정부1·2동, 호원1·2동, 신곡1·2동, 송산1·2·3동)은
# 대표 동으로 통합하고 개별 페이지를 만들지 않는다.
AREAS = [
    ("uijeongbu-dong-chuljangmassage", "의정부동"),
    ("howon-dong-chuljangmassage", "호원동"),
    ("jangam-dong-chuljangmassage", "장암동"),
    ("singok-dong-chuljangmassage", "신곡동"),
    ("songsan-dong-chuljangmassage", "송산동"),
    ("jageum-dong-chuljangmassage", "자금동"),
    ("ganeung-dong-chuljangmassage", "가능동"),
    ("heungseon-dong-chuljangmassage", "흥선동"),
    ("nogyang-dong-chuljangmassage", "녹양동"),
    ("gosan-dong-chuljangmassage", "고산동"),
]

# 지하철역·경전철역 19곳 (slug, 한글명)
# 환승역(회룡역·의정부역)은 노선별로 쪼개지 않고 1개 URL만 생성한다.
STATIONS = [
    ("nogyang-station-chuljangmassage", "녹양역"),
    ("ganeung-station-chuljangmassage", "가능역"),
    ("uijeongbu-station-chuljangmassage", "의정부역"),
    ("hoeryong-station-chuljangmassage", "회룡역"),
    ("mangwolsa-station-chuljangmassage", "망월사역"),
    ("jangam-station-chuljangmassage", "장암역"),
    ("balgok-station-chuljangmassage", "발곡역"),
    ("beomgol-station-chuljangmassage", "범골역"),
    ("uijeongbu-cityhall-station-chuljangmassage", "의정부시청역"),
    ("heungseon-station-chuljangmassage", "흥선역"),
    ("uijeongbu-jungang-station-chuljangmassage", "의정부중앙역"),
    ("dongo-station-chuljangmassage", "동오역"),
    ("saemal-station-chuljangmassage", "새말역"),
    ("northern-gyeonggi-office-station-chuljangmassage", "경기도청북부청사역"),
    ("hyoja-station-chuljangmassage", "효자역"),
    ("gonje-station-chuljangmassage", "곤제역"),
    ("eoryong-station-chuljangmassage", "어룡역"),
    ("songsan-station-chuljangmassage", "송산역"),
    ("tapseok-station-chuljangmassage", "탑석역"),
]


def area_url(slug):
    return f"/uijeongbu/{slug}/"


def station_url(slug):
    return f"/uijeongbu/{slug}/"


# 상단 메뉴 — 하위 메뉴에는 키워드를 반복하지 않고 지역명·역명만 표시한다.
NAV = [
    ("홈", "/", []),
    ("출장마사지 안내", "/#service", [
        ("서비스 안내", "/#service"),
        ("전지역 방문 가능", "/#coverage"),
        ("예약 전 확인 기준", "/#check"),
        ("홈타이 이용 가이드", "/hometai-guide/"),
    ]),
    ("지역별 안내", "/#areas", [
        (name, area_url(slug)) for slug, name in AREAS
    ]),
    ("지하철역별 안내", "/#stations", [
        (name, station_url(slug)) for slug, name in STATIONS
    ]),
    ("예약안내", "/reservation/", [
        ("예약 방법", "/reservation/#how"),
        ("예약 가능 시간", "/reservation/#hours"),
        ("방문 가능 지역", "/reservation/#place"),
        ("결제·이동비 안내", "/reservation/#payment"),
        ("변경·취소 안내", "/reservation/#change"),
    ]),
    ("이용 전 확인사항", "/precautions/", [
        ("방문 전 준비", "/precautions/#prepare"),
        ("외곽 지역 이동 기준", "/precautions/#outer"),
        ("위생·안전 기준", "/precautions/#hygiene"),
        ("자주 묻는 질문", "/precautions/#faq"),
    ]),
    ("고객센터", "/support/", [
        ("공지사항", "/support/#notice"),
        ("자주 묻는 질문", "/support/#faq"),
        ("1:1 문의", "/support/#contact"),
        ("개인정보처리방침", "/privacy/"),
    ]),
]
