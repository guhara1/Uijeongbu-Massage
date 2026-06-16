# 메인 페이지 — 허브 역할. 모든 키워드를 밀어 넣지 않고 상세 페이지로 연결한다.
from .site import (AREAS, BASE_URL, BRAND, NAVER_SITE_VERIFICATION, PHONE,
                   PHONE_DISPLAY, STATIONS, area_url, station_url)
from .pricing import PRICING

# 네이버 서치어드바이저 소유확인 — 메인페이지 head에만 삽입
_NAVER_VERIFY = (
    f'<meta name="naver-site-verification" content="{NAVER_SITE_VERIFICATION}">\n'
)

_AREA_CARDS = "".join(
    f'<li><a href="{area_url(slug)}">{name} 출장마사지</a></li>'
    for slug, name in AREAS
)
_STATION_CARDS = "".join(
    f'<li><a href="{station_url(slug)}">{name} 출장마사지</a></li>'
    for slug, name in STATIONS
)

_JSONLD = f"""{_NAVER_VERIFY}<link rel="preload" as="image" href="/assets/hero.webp" type="image/webp" fetchpriority="high">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "{BRAND}",
  "url": "{BASE_URL}/",
  "telephone": "{PHONE}",
  "image": "{BASE_URL}/assets/og-image.png",
  "logo": "{BASE_URL}/assets/icon-512.png",
  "description": "경기도 의정부시 전지역 방문 출장마사지·홈타이 예약 안내",
  "areaServed": {{
    "@type": "AdministrativeArea",
    "name": "경기도 의정부시"
  }}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "의정부시 전지역 방문이 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "의정부동, 호원동, 장암동, 신곡동, 송산동, 자금동, 가능동, 흥선동, 녹양동, 고산동 등 대표 행정동을 기준으로 의정부시 전지역을 안내합니다. 고산지구·민락지구처럼 차량 이동이 필요한 지역은 이동 기준으로 가능 여부를 확인합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "의정부1동·2동처럼 번호 동은 왜 따로 없나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "의정부1·2동은 의정부동, 호원1·2동은 호원동, 신곡1·2동은 신곡동, 송산1·2·3동은 송산동 대표 페이지로 통합해 중복 페이지 위험을 줄였습니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "회룡역처럼 환승역도 예약할 수 있나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "회룡역은 1호선과 의정부경전철 환승역이지만 노선별로 페이지를 나누지 않고 하나의 회룡역 페이지에서 호원동 생활권과 함께 안내합니다. 의정부역도 1호선·경전철을 한 페이지에서 다룹니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "민락동·금오동도 방문이 되나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "민락동은 송산동·고산동 페이지, 금오동은 자금동 페이지 본문에서 생활권으로 함께 안내합니다. 별도 색인 페이지를 무리하게 늘리지 않고 대표 동 페이지에서 다룹니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "외곽·신도시 지역은 추가 이동비가 있나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "고산지구·민락지구, 장암동 일부처럼 차량 이동 시간이 더 걸리는 지역은 추가 이동비가 발생할 수 있으며, 예약 시 총비용으로 먼저 안내합니다."
      }}
    }}
  ]
}}
</script>
"""

_HERO = f"""<section class="hero">
  <div class="hero-inner hero-grid">
    <div class="hero-text">
      <p class="hero-badge">Premium Visiting Spa · 경기도 의정부시 전지역</p>
      <h1>의정부 출장마사지·의정부시 홈타이<br>지역별 예약 안내</h1>
      <p class="hero-lead">샵까지 갈 필요 없이, 계신 곳에서 받는 방문 관리.<br>의정부시 대표 동과 역세권 어디든 전화 한 통이면 예약이 끝납니다.</p>
      <div class="hero-actions">
        <a class="hero-btn primary" href="tel:{PHONE}">📞 {PHONE_DISPLAY}</a>
        <a class="hero-btn" href="#areas">지역별 안내 보기</a>
      </div>
      <ul class="hero-stats">
        <li><strong>10곳</strong><span>대표 행정동</span></li>
        <li><strong>19개</strong><span>지하철·경전철역</span></li>
        <li><strong>전지역</strong><span>방문 가능</span></li>
        <li><strong>24시간</strong><span>예약 상담</span></li>
      </ul>
    </div>
    <div class="hero-media">
      <picture>
        <source srcset="/assets/hero.webp" type="image/webp">
        <img src="/assets/hero.jpg" alt="의정부 출장마사지·의정부시 홈타이 방문 관리 안내" width="1200" height="675" fetchpriority="high" decoding="async">
      </picture>
    </div>
  </div>
</section>
"""

_BODY = f"""
<section id="service">
<h2>의정부시에서 출장마사지를 찾는 이유</h2>
<p>의정부 출장마사지를 찾는 분들은 대부분 지금 계신 곳에서 가까운 방문 가능 지역을 먼저 확인합니다. 의정부시는 서울 도봉·노원권과 양주, 포천, 남양주 생활권을 잇는 경기북부 중심 도시로, 1호선과 7호선 장암역, 의정부경전철이 함께 지나 이동 동선이 다양한 편입니다. 의정부역과 의정부중앙역 주변은 행복로와 제일시장을 낀 중심 상권이고, 회룡역은 1호선과 경전철을 함께 고려해야 하는 환승 생활권입니다. 송산동과 고산동은 민락지구·고산지구를 포함하는 동부 생활권이며, 자금동은 금오동과 경기도청북부청사 주변까지 함께 보는 것이 좋습니다. {BRAND}는 예약 확인부터 방문 관리까지 정해진 절차에 따라 진행하며, 이 페이지는 의정부 전체 구조를 설명하는 허브 역할을 합니다. 더 자세한 내용은 대표 행정동 페이지와 지하철역·경전철역 페이지에서 확인하실 수 있습니다.</p>
<p>의정부시는 용인처럼 처인구·기흥구·수지구가 있는 도시도, 안양처럼 만안구·동안구가 있는 도시도 아닙니다. 행정구가 없으므로 메인페이지 아래에 바로 대표 행정동 페이지를 두고, 그 아래 지하철역과 경전철역 페이지를 연결하는 구조가 자연스럽습니다.</p>
</section>

<section id="coverage">
<h2>의정부 홈타이 이용 전 확인할 사항</h2>
<p>의정부 홈타이는 자택, 숙소, 사무실 인근에서 예약 가능 여부를 먼저 확인한 뒤 이용하는 방문형 관리 서비스입니다. 의정부동, 호원동, 장암동, 신곡동, 송산동, 자금동, 가능동, 흥선동, 녹양동, 고산동을 각각 대표 지역으로 두고, 페이지마다 생활권과 이동 기준을 다르게 설명합니다. 번호가 붙은 행정동은 개별 페이지로 만들지 않습니다. 의정부1동과 의정부2동은 의정부동으로, 호원1동과 호원2동은 호원동으로, 신곡1동과 신곡2동은 신곡동으로, 송산1·2·3동은 송산동으로 통합해 중복 콘텐츠 위험을 줄였습니다. 같은 본문에서 지역명만 바꾸는 방식은 쓰지 않고, 각 페이지마다 생활권과 이동 기준을 다르게 작성합니다.</p>
</section>

<section id="areas">
<h2>대표 행정동별 방문 가능 지역 안내</h2>
<p>지역별 안내는 의정부시 대표 행정동 10곳을 기준으로 구성됩니다. 각 페이지에서는 해당 생활권의 특징, 가까운 역, 방문 전 확인사항, 예약 가능 시간, 추가 이동비 여부를 지역마다 고유한 내용으로 설명합니다. 거주하시거나 머무시는 지역을 선택해 주세요.</p>
<ul class="card-grid">
{_AREA_CARDS}
</ul>
<p>의정부동은 의정부역·중앙로 중심 상권을, 호원동은 회룡역·망월사역 생활권을, 신곡동은 의정부시청·동오 생활권을, 송산동은 민락·용현·탑석 동부 생활권을, 자금동은 금오동·경기도청북부청사 주변을, 고산동은 고산지구·민락 인접권을 중심으로 안내합니다.</p>
</section>

<section id="stations">
<h2>의정부역·회룡역·가능역·탑석역 역세권 안내</h2>
<p>지하철역별 안내는 의정부시를 지나는 1호선, 7호선 장암역, 의정부경전철 역세권을 기준으로 구성합니다. 각 역 페이지에서는 주변 행정동, 이동 동선, 이용 시간대, 예약 전 확인사항을 역마다 다르게 설명하며, 역 이름만 바꾼 반복 페이지나 노선·방향별 중복 페이지는 만들지 않습니다. 회룡역은 1호선·경전철 환승역이지만 1개 URL로만, 의정부역도 경전철의정부역과 과하게 분리하지 않고 1개 URL로 안내합니다.</p>
<ul class="card-grid">
{_STATION_CARDS}
</ul>
<p>의정부역은 중심 상권과, 회룡역은 호원동 환승 생활권과, 가능역·흥선역은 가능동·흥선동 생활권과, 녹양역은 녹양동·종합운동장과, 탑석역·송산역은 송산동·고산지구 동부 생활권과 연결됩니다.</p>
</section>

<section id="living">
<h2>민락·고산·금오 생활권을 본문에서 다루는 방식</h2>
<p>민락동, 용현동, 금오동, 낙양동처럼 검색 수요가 생길 수 있는 법정동·생활권은 처음부터 별도 페이지를 많이 만들기보다, 가까운 대표 동 페이지 본문에서 세부 생활권으로 다룹니다. 민락동은 송산동·고산동 페이지에서, 용현동은 송산동 페이지에서, 금오동은 자금동 페이지에서, 낙양동은 고산동 페이지에서 자연스럽게 설명합니다. 이렇게 하면 얇은 지역 페이지를 한꺼번에 대량으로 색인시키는 위험을 피하면서도, 실제 생활권 정보를 충실히 전달할 수 있습니다. 검색 데이터가 충분히 쌓이면 이후에 민락 생활권 페이지를 별도로 확장할 수 있습니다.</p>
</section>

<section id="check">
<h2>예약 전 꼭 확인해야 할 기준</h2>
<p>예약 전에는 방문 가능 지역, 관리 가능 시간, 추가 이동비, 결제 방식, 취소 기준, 서비스 범위를 먼저 확인해야 합니다. 의정부시는 도시 면적이 아주 큰 편은 아니지만, 의정부역 중심권, 호원·회룡 생활권, 송산·민락·고산 동부 생활권, 녹양·가능 북서부 생활권의 이동 기준이 서로 다릅니다. 특히 고산동, 민락동, 장암동 일부는 차량 이동 시간이 달라질 수 있으므로, 자세한 준비 방법은 <a href="/precautions/">이용 전 확인사항</a>에서, 예약 절차와 결제·이동비 안내는 <a href="/reservation/">예약안내</a>에서 확인해 주세요. 홈타이가 처음이라면 <a href="/hometai-guide/">홈타이 이용 가이드</a>를 함께 보시면 도움이 됩니다.</p>
</section>

<section id="guide">
<h2>의정부 출장마사지 사이트 이용 가이드</h2>
<p>메인페이지는 의정부시 전체 안내를 담당하고, 대표 행정동 페이지는 의정부동·호원동·신곡동·송산동·자금동·가능동·흥선동·녹양동·고산동 등 세부 지역 검색을, 지하철역·경전철역 페이지는 의정부역·회룡역·가능역·녹양역·탑석역 등 실제 검색 의도를 담당합니다. 거주 지역이 익숙하면 행정동 페이지를, 역 기준 위치가 익숙하면 역세권 페이지를 보시면 됩니다. 어느 페이지를 보셔도 예약 절차와 비용 기준은 동일하며, 최종 안내는 언제나 정확한 주소를 기준으로 이루어집니다. 과장된 표현이나 허위 후기, 불법·선정적인 안내는 사용하지 않으며, 이용 가능 지역과 예약 절차, 취소 기준, 개인정보 처리 기준을 분명하게 보여드리는 것을 원칙으로 합니다.</p>
</section>

<section id="faq">
<h2>자주 묻는 질문</h2>
<div class="faq-item">
<h3>의정부시 전지역 방문이 가능한가요?</h3>
<p>대표 행정동 10곳과 지하철·경전철역 19곳을 기준으로 의정부시 전지역을 안내합니다. 고산지구·민락지구처럼 차량 이동이 필요한 지역은 이동 기준으로 가능 여부를 확인합니다.</p>
</div>
<div class="faq-item">
<h3>의정부1동·호원1동처럼 번호 동은 왜 페이지가 없나요?</h3>
<p>의정부1·2동은 의정부동, 호원1·2동은 호원동, 신곡1·2동은 신곡동, 송산1·2·3동은 송산동 대표 페이지에서 통합 안내합니다. 같은 생활권을 나눠 반복 설명하지 않기 위해서입니다.</p>
</div>
<div class="faq-item">
<h3>회룡역·의정부역 같은 환승역은 어떻게 안내하나요?</h3>
<p>회룡역은 1호선·경전철 환승역이지만 노선별로 나누지 않고 하나의 페이지에서 호원동 생활권과 함께 안내합니다. 의정부역도 1호선과 경전철을 한 페이지에서 다룹니다.</p>
</div>
<div class="faq-item">
<h3>고산동·민락동 같은 지역은 추가 이동비가 붙나요?</h3>
<p>고산지구·민락지구, 장암동 일부처럼 차량 이동 시간이 더 걸리는 지역은 추가 이동비가 발생할 수 있습니다. 예약 시 총비용으로 먼저 안내해 드립니다.</p>
</div>
</section>

{PRICING}
<section id="contact" class="cta">
<h2>예약문의</h2>
<p>의정부 방문 관리 예약과 상담은 전화로 가장 빠르게 진행됩니다. 위치와 희망 시간을 알려주시면 가능 여부를 바로 확인해 드립니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""

PAGE = {
    "path": "",
    "title": "의정부 출장마사지｜의정부시 홈타이 지역별 예약 안내",
    "desc": "의정부 출장마사지·홈타이 예약 전 대표 동, 역세권, 이용 기준을 정리했습니다.",
    "h1": "의정부 출장마사지 · 의정부시 홈타이 지역별 예약 안내",
    "body": _BODY,
    "extra_head": _JSONLD,
    "breadcrumb": [],
    "hero": _HERO,
}
