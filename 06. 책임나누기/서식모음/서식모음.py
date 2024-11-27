from 서식33 import 서식33인턴신청서
from 서식46 import 서식46인턴확인서
from enum import Enum

# Enum을 사용하여 서식 이름과 매핑되는 키를 정의합니다.
class 서식이름(Enum):
    서식33 = "[서식33] 인턴형 일경험 참여신청서"
    서식46 = "[서식46] 인턴형 참여청년 확인서"

class 서식모음:
    def __init__(self):
        # 서식을 딕셔너리로 관리하여 나중에 쉽게 추가하거나 접근할 수 있도록 합니다.
        self.서식들 = {
            서식이름.서식33.value: 서식33인턴신청서,
            서식이름.서식46.value: 서식46인턴확인서
        }

    def 실행(self, 서식명, excel_path, form_path):
        # 선택된 서식을 실행하는 함수입니다.
        if 서식명 in self.서식들:
            self.서식들[서식명](excel_path, form_path)
        else:
            print(f"지원하지 않는 서식입니다: {서식명}")