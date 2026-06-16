# 지하철역·경전철역 19개 페이지 집계.
# 역 이름만 바꾼 반복/노선·방향별 중복 페이지는 만들지 않는다.
from .stations_g1 import PAGES as _S1
from .stations_g2 import PAGES as _S2

PAGES = _S1 + _S2
