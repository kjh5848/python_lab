from excel_service import ExcelService
from hwp_service import HwpService
import os


def 서식46인턴확인서(self, excel_path, form_path):
    for index, row in self.excel_service.엑셀열기(excel_path, "참여자 명단").iterrows():
        self.hwp_service.파일열기("[서식46] 인턴형 참여청년 확인서", os.path.dirname(form_path))

        if not row['성명']:
            print(f"빈 값 발견 - 행 {index + 1} 건너뜀")
            continue

        try:
            self.hwp_service.채우기('성명', row['성명'])
            self.hwp_service.채우기('생년월일', row['생년월일'])
            new_file_name = f'[서식46] 인턴형 참여청년 확인서_{row["성명"]}.hwp'
            self.hwp_service.저장(new_file_name, os.path.dirname(form_path))
            self.hwp_service.닫기()
        except Exception as e:
            print(f"오류 발생 (행 {index + 1}): {e}")