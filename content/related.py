# 내부링크 강화 컴포넌트 — 지역·역세권 페이지 상호 연결(롱테일 앵커)
# 모든 지역/역 페이지 하단에 삽입되어 사이트 내부 링크 구조(사일로)를 강화한다.
from .site import AREAS, STATIONS, area_url, station_url


def related_block(current_slug=None):
    """현재 페이지를 제외한 전 행정동·역세권으로의 롱테일 내부링크 블록.

    행정동은 '○○ 출장마사지', 역세권은 '○○ 홈타이' 로 앵커 텍스트를 분산해
    동일 앵커 반복을 피하면서 지역 키워드를 고르게 연결한다."""
    area_links = "".join(
        f'<li><a href="{area_url(s)}">{n} 출장마사지</a></li>'
        for s, n in AREAS if s != current_slug
    )
    station_links = "".join(
        f'<li><a href="{station_url(s)}">{n} 홈타이</a></li>'
        for s, n in STATIONS if s != current_slug
    )
    return f"""
<section class="related-areas" aria-label="주변 지역·역세권 안내">
<h2>의정부 지역·역세권 출장마사지 함께 보기</h2>
<p>가까운 행정동과 지하철·경전철역 안내를 함께 확인하시면, 거주하거나 머무시는 위치에 맞는 방문 가능 여부와 이동 기준, 추가 이동비를 빠르게 비교하실 수 있습니다. 의정부시 전지역을 같은 기준으로 안내해 드립니다.</p>
<div class="related-grid">
  <nav class="related-col" aria-label="행정동별 안내">
    <p class="related-title">행정동별 출장마사지</p>
    <ul class="related-list">{area_links}</ul>
  </nav>
  <nav class="related-col" aria-label="역세권별 안내">
    <p class="related-title">역세권별 홈타이</p>
    <ul class="related-list">{station_links}</ul>
  </nav>
</div>
</section>
"""
