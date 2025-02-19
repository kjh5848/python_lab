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


    def insert_signature_image(self, image_path, target_field_name, width=19, height=19, x_pos=0, y_pos=0):
        """지정된 필드에 서명 이미지 삽입 및 크기/위치 설정"""
        try:
            # 서명 필드로 이동
            self.hwp.MoveToField(target_field_name)

            # 이미지 삽입
            self.hwp.InsertPicture(image_path, Embedded=True, sizeoption=0)
            
            # 개체 선택
            self.hwp.FindCtrl()  
            
            # 설정 변경
            self.hwp.HAction.GetDefault("ShapeObjDialog", self.hwp.HParameterSet.HShapeObject.HSet)
            # self.hwp.HParameterSet.HShapeObject.HSet.SetItem("Height", int(height * 283.465))  # 높이 설정
            # self.hwp.HParameterSet.HShapeObject.HSet.SetItem("Width", int(width * 283.465))   # 너비 설정
            self.hwp.HParameterSet.HShapeObject.HSet.SetItem("TreatAsChar", 0)  # 글자처럼 취급 해제
            self.hwp.HParameterSet.HShapeObject.HSet.SetItem("TextWrap", 3)  # 글 앞에 배치
            self.hwp.HParameterSet.HShapeObject.HSet.SetItem("HorzRelTo", 0)  # 종이 기준 위치 설정
            self.hwp.HParameterSet.HShapeObject.HSet.SetItem("VertRelTo", 0)
            # self.hwp.HParameterSet.HShapeObject.HSet.SetItem("HorzOffset", self.hwp.MiliToHwpUnit(x_pos))
            # self.hwp.HParameterSet.HShapeObject.HSet.SetItem("VertOffset", self.hwp.MiliToHwpUnit(y_pos))
            
            # 설정 적용
            self.hwp.HAction.Execute("ShapeObjDialog", self.hwp.HParameterSet.HShapeObject.HSet)

            print(f"서명 이미지 삽입 완료: '{target_field_name}' 필드")
        except Exception as e:
            print(f"이미지 삽입 오류 ({target_field_name}): {e}")

    def 필드에_이미지_삽입(self, field_names, image_dir, name ):
        """필드명이 {서명}이고, 성명과 같은 이미지 파일이 있으면 삽입"""

        valid_extensions = [".jpg", ".png", ".jpeg"]

        # {서명} 필드가 있는지 확인
        if "서명" in field_names:
            image_path = None
            for ext in valid_extensions:
                temp_path = os.path.join(image_dir, f"{name}{ext}")
                if os.path.exists(temp_path):
                    image_path = temp_path
                    break  # 존재하는 파일을 찾으면 반복 종료

            if image_path:
                self.insert_signature_image(image_path, "서명")
            else:
                print(f"이미지 없음: {name}")  # 동일한 필드는 한 번만 삽입  # 동일한 필드는 한 번만 삽입
                

    def 필드채우기(self, field_names, row_data):
        """HWP 필드에 데이터 채우기"""
        for field_name in field_names:
            if field_name in row_data.index:
                value = self._포맷팅(row_data[field_name])
                self.채우기(field_name, value)

    def 홀짝필드채우기(self,excel_sheet,field_names):
        for row_index, row_data in excel_sheet.iterrows():
            try:
                # 열 순회: 모든 열에서 필드명, 값 쌍으로 처리
                for col_index in range(1, len(row_data), 2):  # 2칸씩 건너뛰기 (필드명, 값 쌍)
                    field_name = row_data[col_index]  # 현재 열 (필드명)
                    if col_index + 1 < len(row_data):  # 값 열이 존재하는지 확인
                        field_value = row_data[col_index + 1]
                    else:
                        continue  # 값 열이 없으면 스킵

                    # 필드 이름이 한글 필드 목록에 있는 경우만 처리
                    if field_name in field_names:
                        self.채우기(field_name, self._포맷팅(field_value))

            except Exception as e:
                print(f"오류 발생 (사전직무정보 행: {row_index + 1}, 열: {col_index}): {e}")

    def fill_fields(self, data, field_mapping):
        """시작하는 필드 이름을 동적으로 매핑하여 데이터를 채우기."""
        for index, row in data.iterrows():
            try:
                for excel_col, hwp_fields in field_mapping.items():
                    if index < len(hwp_fields):
                        hwp_field_name = hwp_fields[index]
                        self.채우기(hwp_field_name, row[excel_col])
            except Exception as e:
                print(f"오류 발생 (행: {index + 1}, 필드: {excel_col}): {e}")

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
            if "%" in str(cell_data):  # 만약 퍼센트 기호가 포함된 데이터라면
                return str(int(float(cell_data.strip("%")))) + "%"
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

    def 한칸아래로(self):
        """현재 커서를 한 칸 아래로 이동"""
        try:
            self.hwp.HAction.Run("MoveDown")  # 한글의 '아래로 한 칸 이동' 액션 실행
        except Exception as e:
            print(f"한 칸 아래로 이동 중 오류 발생: {e}")
    
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
    



