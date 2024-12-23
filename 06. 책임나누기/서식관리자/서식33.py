from excel_service import ExcelService
from hwp_service import HwpService
import os

def 서식33인턴신청서(self, excel_path, form_path):
        for index, row in self.excel_service.엑셀열기(excel_path, "참여자 명단",0).iterrows():
            self.hwp_service.파일열기("[서식33] 인턴형 일경험 참여신청서", os.path.dirname(form_path))
            
            if not row['성명']:
                print(f"빈 값 발견 - 행 {index + 1} 건너뜀")
                continue

            try:
                self.hwp_service.채우기('성명', row['성명'])

                # 다른 필드들도 동일하게 채우기...
                new_file_name = f'[서식33] 인턴형 일경험 참여신청서_{row["성명"]}.hwp'
                self.hwp_service.저장(new_file_name, os.path.dirname(form_path))
                self.hwp_service.닫기()
            except Exception as e:
                print(f"오류 발생 (행 {index + 1}): {e}")