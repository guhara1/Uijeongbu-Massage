# 간다GO — 의정부 출장마사지·의정부시 홈타이 지역 SEO 사이트

경기도 의정부시에서 방문형 마사지(출장마사지)·홈타이를 찾는 사용자가 현재 위치에
맞는 대표 행정동, 1호선·7호선·의정부경전철 역세권 정보를 쉽게 확인할 수 있도록 만든
정적 지역 SEO 사이트입니다.

- **상호:** 간다GO
- **예약전화:** 0508-202-4719
- **핵심 키워드:** 출장마사지 / **보조:** 홈타이
- **지역 키워드:** 의정부 출장마사지, 의정부시 출장마사지, 의정부 홈타이

## 구조 (총 35페이지)

```
메인 1
대표 행정동 10   (의정부동·호원동·장암동·신곡동·송산동·
                  자금동·가능동·흥선동·녹양동·고산동)
역세권 19        (1호선: 녹양·가능·의정부·회룡·망월사
                  7호선: 장암
                  경전철: 발곡·범골·의정부시청·흥선·의정부중앙·동오·새말·
                          경기도청북부청사·효자·곤제·어룡·송산·탑석)
안내 페이지 5    (예약안내·이용 전 확인사항·홈타이 이용 가이드·
                  개인정보처리방침·고객센터)
```

번호 행정동(의정부1·2동, 호원1·2동, 신곡1·2동, 송산1·2·3동)은 개별 페이지를 만들지
않고 대표 동으로 통합합니다. 민락동·용현동·금오동·낙양동 등 법정동·생활권은 가까운
대표 동 페이지 본문에서 보조 설명으로 처리합니다.

## 환승역·중복역 처리

- **회룡역**: 1호선·의정부경전철 환승이지만 1개 URL만 생성, 노선별로 나누지 않음
- **의정부역**: 1호선과 경전철의정부역을 과하게 분리하지 않고 1개 URL로 안내
- **장암역**: 7호선 역세권 1개 URL만 생성
- **탑석역**: 의정부경전철 기준 1개 URL만 생성
- 예정 노선(7호선 연장, GTX-C)·예정역은 단독 색인 페이지를 만들지 않고 본문 보조 설명으로만 처리

## URL 규칙

| 구분 | 경로 |
|------|------|
| 메인 | `/` |
| 대표 행정동 | `/uijeongbu/<slug>-chuljangmassage/` |
| 역세권 | `/uijeongbu/<station>-station-chuljangmassage/` |

> 메인페이지는 배포 도메인 루트(`/`)에 위치합니다. 워드프레스 슬러그
> `/uijeongbu-chuljangmassage/`로 운영하려면 해당 경로로 리다이렉트하세요.

## 빌드

```bash
python3 build.py
```

`content/` 패키지의 페이지 정의를 읽어 각 경로에 `index.html`을 생성하고
`sitemap.xml`, `robots.txt`, `.nojekyll`을 갱신합니다.

- 본문 텍스트 2,000자 미만 페이지는 자동으로 `noindex` 처리됩니다.
- 모든 페이지에 `WebPage`·`BreadcrumbList` 구조화 데이터가 자동 삽입되고,
  메인에는 `Organization`·`FAQPage`가 추가됩니다.
- 오프라인 매장 주소가 없으므로 `LocalBusiness` 스키마는 사용하지 않습니다.

## 배포 전 설정

- `content/site.py`의 `BASE_URL`을 실제 도메인으로 변경한 뒤 `python3 build.py` 재실행.

## 디렉터리

```
build.py            빌드 스크립트
content/            페이지 정의 (site, main, areas_g1/g2, stations_g1/g2, info, pricing)
assets/             style.css, nav.js, 파비콘/OG 이미지
scripts/            색인 통보 스크립트 (indexnow, google_indexing)
.github/workflows/  푸시 시 자동 색인 통보 (indexing.yml)
```

## 검색 색인 / 빠른 인덱싱

빌드 시 다음 색인 자산이 자동 생성됩니다.

| 파일 | 용도 |
|------|------|
| `sitemap.xml` | 표준 사이트맵 (`lastmod`·`changefreq`·`priority` 포함) |
| `rss.xml` | RSS 피드 — 구글·네이버 신규/갱신 콘텐츠 발견 가속 |
| `robots.txt` | Googlebot·Bingbot·**Yeti(네이버)**·Daum 명시 허용 + 사이트맵·RSS 안내 |
| `<INDEXNOW_KEY>.txt` | IndexNow 인증 키 파일 (루트 게시) |

### 1) IndexNow — 빙·네이버 즉시 통보 (구글 미참여)

키 파일이 도메인 루트에 게시된 상태에서:

```bash
python3 scripts/indexnow.py --all       # sitemap 전체 통보
python3 scripts/indexnow.py --changed   # 직전 커밋 대비 변경분만 통보
python3 scripts/indexnow.py <URL> ...   # 특정 URL 통보
```

한 번 통보하면 IndexNow 참여 검색엔진(빙·**네이버**·얀덱스 등)에 전파됩니다.
별도 시크릿이 필요 없습니다.

### 2) 구글 Indexing API — 구글 직접 통보

1. Google Cloud에서 **Indexing API** 사용 설정 → 서비스 계정 생성 → JSON 키 발급
2. **Search Console** 속성에 서비스 계정 이메일을 *소유자*로 추가
3. 실행:

```bash
pip install -r scripts/requirements.txt
export GOOGLE_APPLICATION_CREDENTIALS=서비스계정.json
python3 scripts/google_indexing.py --all       # 또는 --changed / <URL>
```

> 참고: Indexing API는 공식적으로 JobPosting·BroadcastEvent용이며 일반 URL 통보는
> 보장되지 않습니다. 구글 색인의 정식 경로는 **Search Console + 사이트맵 제출**이고,
> 본 스크립트는 발견 가속용 보조 수단입니다.

### 3) 자동화 — 푸시할 때마다 즉시 통보

`.github/workflows/indexing.yml` 가 `main`/`master` 푸시 시(또는 수동 실행 시)
배포 전파를 기다린 뒤 **변경된 URL만** IndexNow로 통보합니다. 구글 통보까지 켜려면
저장소 시크릿 `GOOGLE_INDEXING_CREDENTIALS`(서비스 계정 JSON 전체)을 추가하세요.
시크릿이 없으면 IndexNow만 동작하고 구글 단계는 자동으로 건너뜁니다.

> Cloudflare Pages는 저장소에서 정적 파일을 그대로 배포하므로 별도 빌드 명령이
> 필요 없습니다(이미 HTML이 커밋되어 있음). 워크플로의 `sleep`는 키 파일·신규
> 페이지가 도메인에 반영될 시간을 확보하기 위한 것입니다.

### 배포 후 1회 권장 작업

1. **구글 Search Console** 속성 등록 → `sitemap.xml` 제출
2. **네이버 서치어드바이저** 사이트 등록 → 사이트맵 `sitemap.xml`·RSS `rss.xml` 제출
3. **빙 웹마스터 도구** 등록(IndexNow 키 자동 인식)
4. 첫 통보: `python3 scripts/indexnow.py --all`
