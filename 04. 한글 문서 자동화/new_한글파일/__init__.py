# %%
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))  # 현재 파일 경로
util_dir = os.path.join(current_dir, '..', 'utill')  # 상위 디렉토리에서 'utill' 폴더 경로 생성
sys.path.append(util_dir)

print(sys.path)

# %%
