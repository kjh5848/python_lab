import win32com.client as win32
import os
import pandas as pd

class HwpUtill:
    def __init__(self):
        self.hwp = win32.gencache.EnsureDispatch("hwpframe.hwpobject")
        self.hwp.RegisterModule("FilePathCheckDLL", "FilePathCheckerModuleExample")
        self.hwp.XHwpWindows.Item(0).Visible = True  # 한글 창을 보이게 설정
    

    def 학력정보입력(self, row):
        학력구분 = row.get('최종학력구분', "")
        학력상태 = row.get('최종학력상태', "")
        학년 = row.get('학년', "")


        # 대학교 관련 처리
        if 학력구분 in ['대학교_4년제', '대학교_2년제', '대학교_2/3년제']:
            self.채우기('대학교', '■')
            self.채우기('대학교명', row.get('최종학교명', ''))

            if 학력상태 == '졸업':
                self.채우기('대학교졸업', '■')
            elif 학력상태 == '졸업예정자':
                self.채우기('졸업예정자', '■')
            elif 학력상태 in ['휴학', '재학']:
                학년필드 = '재학(1~2학년)' if 학년 in ['1', '2'] else '재학(3~4학년)'
                self.채우기(학년필드, '■')

        # 고등학교 관련 처리
        elif 학력구분 == '고등학교':
            self.채우기('고등학교', '■')
            self.채우기('고등학교명', row.get('최종학교명', ''))

            if 학력상태 == '졸업':
                self.채우기('고등학교졸업', '■')
            elif 학력상태 == '졸업예정자':
                self.채우기('고등학교졸업예정자', '■')
            elif 학력상태 == '재학':
                학년필드 = '고등학교재학(1~2학년)' if 학년 in ['1', '2'] else '고등학교재학(3학년)'
                self.채우기(학년필드, '■')
            elif 학력상태 == '검정고시':
                self.채우기('검정고시', '■')



    def 저장파일열기(self,save_file_path):
        os.startfile(save_file_path)


    def 필드가져오기(self, file_name, file_path):
        """HWP 파일에서 필드 목록 가져오기"""
        self.파일열기(file_name=file_name, file_path=file_path)
        field_list = self.hwp.GetFieldList().split('\x02')
        return [field.split('\x00')[0] for field in field_list]


    def 필드채우기(self, field_names, row_data):
        """HWP 필드에 데이터 채우기"""
        for field_name in field_names:
            if field_name in row_data.index:
                value = self._포맷팅(row_data[field_name])
                self.채우기(field_name, value)

    def 채우기(self, field_name, value):
        """필드에 값 입력"""
        try:
            self.hwp.PutFieldText(field_name, value)
        except Exception as e:
            print(f"Error filling field {field_name}: {e}")

    # 포맷팅 메서드
    def _포맷팅(self, cell_data):
        """셀 데이터 포맷팅"""
        if pd.isna(cell_data):
            return ""
        elif isinstance(cell_data, (int, float)):
            return f"{int(cell_data)}" if cell_data % 1 == 0 else f"{cell_data:.2f}"
        return str(cell_data)


     # 희망 직무 입력
    def 희망직무(self, row):
        """희망 직무에 따라 필드 채우기"""
        직무 = row.get('직무', "")
        if 직무 == 'IT':
            self.채우기('IT', '■')
        elif 직무 == '광고 마케팅':
            self.채우기('광고 마케팅', '■')



    def 파일열기(self, file_name, file_path):
        file_path = fr'{file_path}\{file_name}.hwp'
        return self.hwp.Open(file_path)


    
    def 세로누름틀생성(self, 시작인덱스 , 필드이름, 개수):
        for i in range(개수):
            field_name = f"{필드이름}_{시작인덱스 + i}"
            self.hwp.CreateField(필드이름, "", field_name)
            self.hwp.HAction.Execute("MoveDown", self.hwp.HParameterSet.HFindReplace.HSet)


    def 가로누름틀생성한줄(self, 시작인덱스, 안내문, 필드이름, 개수):
        for i in range(개수):
            # 필드 이름 생성
            field_name = f"{필드이름}_{시작인덱스 + i}"
            
            # 누름틀 필드 생성 (현재 커서 위치에 삽입)
            self.hwp.CreateField(안내문, "", field_name)
            print(f"Inserted field: {field_name}")
            
            # 누름틀 생성 후 커서를 누름틀 바깥으로 이동
            self.hwp.HAction.Run("MoveRight")  # 누름틀 뒤로 커서 이동
            
            # 표의 다음 칸으로 이동
            if i < 개수 - 1:  # 마지막 필드 후에는 이동하지 않음
                self.hwp.HAction.Run("TableRightCell")  # 표의 다음 칸으로 이동
                


    def 저장폴더(self,save_file_path):
        if not os.path.exists(save_file_path):
            os.makedirs(save_file_path)


    def 저장(self, new_file_name, save_file_path):
        """HWP 파일 저장"""
        if not os.path.exists(save_file_path):
            os.makedirs(save_file_path)
        try:
            self.hwp.SaveAs(os.path.join(save_file_path, new_file_name))
            print(f'파일 저장 완료: {new_file_name}')
        except Exception as e:
            print(f"Error saving file {new_file_name}: {e}")


    def 닫기(self):
        self.hwp.Clear(1)


    def 종료(self):
        self.hwp.Quit()

    
    def 초기화(self):
        """누름틀 필드를 모두 초기화"""
        try:
            field_list = self.hwp.GetFieldList().split('\x02')
            for field_name in field_list:
                self.hwp.PutFieldText(field_name, "")  # 각 누름틀 필드의 내용을 빈 값으로 설정
            print("모든 누름틀 초기화 완료")
        except Exception as e:
            print(f"초기화 오류: {e}")


        # 학력 정보 입력 관련 메서드
    



