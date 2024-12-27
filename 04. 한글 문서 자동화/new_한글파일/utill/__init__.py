# %%
import os
import sys

# 현재 파일 위치를 기준으로 상위 디렉토리 경로를 계산
current_dir = os.path.dirname(os.path.abspath(__file__))
util_dir = os.path.join(current_dir)

# 경로를 sys.path에 추가
if util_dir not in sys.path:
    sys.path.append(util_dir)

# 디버그용으로 sys.path 확인
print("현재 sys.path:", sys.path)
# %%
