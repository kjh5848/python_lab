import win32com.client as win32
import os

class HwpUtill:
    def __init__(self):
        self.hwp = win32.gencache.EnsureDispatch("hwpframe.hwpobject")
        self.hwp.RegisterModule("FilePathCheckDLL", "FilePathCheckerModuleExample")
        self.hwp.XHwpWindows.Item(0).Visible = True  # 한글 창을 보이게 설정

    def 파일열기(self, file_name, file_path):
        file_path = fr'{file_path}\{file_name}.hwp'
        return self.hwp.Open(file_path)

    def 채우기(self, field_name, value):
        try:
            self.hwp.PutFieldText(field_name, value)
        except Exception as e:
            print(f"Error filling field {field_name}: {e}")

    def 저장(self, new_file_name, new_file_path):
        try:
            self.hwp.SaveAs(os.path.join(new_file_path, new_file_name))
            print(f'파일 저장 완료: {new_file_name}')
        except Exception as e:
            print(f"Error saving file {new_file_name}: {e}")
    
    def 세로누름틀생성(self, 시작인덱스 , 필드이름, 개수):
        for i in range(개수):
            field_name = f"{필드이름}_{시작인덱스 + i}"
            self.hwp.CreateField(필드이름, "", field_name)
            self.hwp.HAction.Execute("MoveDown", self.hwp.HParameterSet.HFindReplace.HSet)

    def 가로누름틀생성한줄(self, 시작인덱스, 필드이름, 개수):
        for i in range(개수):
            # 필드 이름 생성
            field_name = f"{필드이름}_{시작인덱스 + i}"
            
            # 누름틀 필드 생성 (현재 커서 위치에 삽입)
            self.hwp.CreateField(필드이름, "", field_name)
            print(f"Inserted field: {field_name}")
            
            # 누름틀 생성 후 커서를 누름틀 바깥으로 이동
            self.hwp.HAction.Run("MoveRight")  # 누름틀 뒤로 커서 이동
            
            # 표의 다음 칸으로 이동
            if i < 개수 - 1:  # 마지막 필드 후에는 이동하지 않음
                self.hwp.HAction.Run("TableRightCell")  # 표의 다음 칸으로 이동


    def 닫기(self):
        self.hwp.Clear(1)

    def 종료(self):
        self.hwp.Quit()
    
    def 초기화(self,excel,select_row_index):
        
        for index, row in excel.iterrows():
            # A, B열 데이터 삽입
            self.hwp.PutFieldText(select_row_index,"")  # A열: 필드명, B열: 값




    def 학력정보입력(self, row):
        """최종학력구분 및 상태에 따라 한글 필드 채우기"""
        try:
            # 대학교_4년제
            if row['최종학력구분'] == '대학교_4년제':
                self.hwp.PutFieldText('대학교', '■')
                self.hwp.PutFieldText('대학교명', row['최종학교명'])

                if row['최종학력상태'] == '졸업':
                    self.hwp.PutFieldText('대학교졸업', '■')
                elif row['최종학력상태'] == '졸업예정자':
                    self.hwp.PutFieldText('졸업예정자', '■')
                elif row['최종학력상태'] in ['휴학', '재학']:
                    if row['학년'] in ['1', '2']:
                        self.hwp.PutFieldText('재학(1~2학년)', '■')
                    elif row['학년'] in ['3', '4']:
                        self.hwp.PutFieldText('재학(3~4학년)', '■')

            # 대학교_2년제 또는 대학교_2/3년제
            elif row['최종학력구분'] in ['대학교_2년제', '대학교_2/3년제']:
                self.hwp.PutFieldText('대학교', '■')
                self.hwp.PutFieldText('대학교명', row['최종학교명'])

                if row['최종학력상태'] == '졸업':
                    self.hwp.PutFieldText('대학교졸업', '■')
                elif row['최종학력상태'] == '졸업예정자':
                    self.hwp.PutFieldText('졸업예정자', '■')
                elif row['최종학력상태'] in ['휴학', '재학']:
                    if row['학년'] in ['1', '2']:
                        self.hwp.PutFieldText('재학(1~2학년)', '■')
                    elif row['학년'] == '3':
                        self.hwp.PutFieldText('재학(3~4학년)', '■')

            # 고등학교
            elif row['최종학력구분'] == '고등학교':
                self.hwp.PutFieldText('고등학교', '■')
                self.hwp.PutFieldText('고등학교명', row['최종학교명'])

                if row['최종학력상태'] == '졸업':
                    self.hwp.PutFieldText('고등학교졸업', '■')
                elif row['최종학력상태'] == '졸업예정자':
                    self.hwp.PutFieldText('고등학교졸업예정자', '■')
                elif row['최종학력상태'] == '재학':
                    if row['학년'] in ['1', '2']:
                        self.hwp.PutFieldText('고등학교재학(1~2학년)', '■')
                    elif row['학년'] == '3':
                        self.hwp.PutFieldText('고등학교재학(3학년)', '■')
                elif row['최종학력상태'] == '검정고시':
                    self.hwp.PutFieldText('검정고시', '■')

            # 예외 처리
            else:
                print(f"알 수 없는 학력 구분: {row['최종학력구분']}")

        except KeyError as e:
            print(f"필드 누락: {e}")
        except Exception as e:
            print(f"학력정보 입력 오류: {e}")


    def 학력정보입력_4년제(self, row):
        """최종학력구분 및 상태에 따라 한글 필드 채우기"""
        try:
            if row['최종학력구분'] == '대학교_4년제':
                self.hwp.PutFieldText('대학교', '■')
                self.hwp.PutFieldText('대학교명', row['최종학교명'])

                if row['최종학력상태'] == '졸업':
                    self.hwp.PutFieldText('대학교졸업', '■')
                elif row['최종학력상태'] == '졸업예정자':
                    self.hwp.PutFieldText('졸업예정자', '■')
                elif row['최종학력상태'] in ['휴학', '재학']:
                    if row['학년'] in ['1', '2']:
                        self.hwp.PutFieldText('재학(1~2학년)', '■')
                    elif row['학년'] in ['3', '4']:
                        self.hwp.PutFieldText('재학(3~4학년)', '■')

        except KeyError as e:
            print(f"필드 누락: {e}")
        except Exception as e:
            print(f"학력정보입력_4년제 오류: {e}")
    
    def 학력정보입력_2_3년제(self, row):
        """최종학력구분 및 상태에 따라 한글 필드 채우기"""
        try:
            
            if row['최종학력구분'] in ['대학교_2년제', '대학교_2/3년제']:
                self.hwp.PutFieldText('대학교', '■')
                self.hwp.PutFieldText('대학교명', row['최종학교명'])

                if row['최종학력상태'] == '졸업':
                    self.hwp.PutFieldText('대학교졸업', '■')
                elif row['최종학력상태'] == '졸업예정자':
                    self.hwp.PutFieldText('졸업예정자', '■')
                elif row['최종학력상태'] in ['휴학', '재학']:
                    if row['학년'] in ['1', '2']:
                        self.hwp.PutFieldText('재학(1~2학년)', '■')
                    elif row['학년'] in ['3']:
                        self.hwp.PutFieldText('재학(3~4학년)', '■')

            elif row['최종학력구분'] == '고등학교':
                self.hwp.PutFieldText('고등학교', '■')
                self.hwp.PutFieldText('고등학교명', row['최종학교명'])

                if row['최종학력상태'] == '졸업':
                    self.hwp.PutFieldText('고등학교졸업', '■')
                elif row['최종학력상태'] == '졸업예정자':
                    self.hwp.PutFieldText('고등학교졸업예정자', '■')
                elif row['최종학력상태'] == '재학':
                    if row['학년'] in ['1', '2']:
                        self.hwp.PutFieldText('고등학교재학(1~2학년)', '■')
                    elif row['학년'] == '3':
                        self.hwp.PutFieldText('고등학교재학(3학년)', '■')
                elif row['최종학력상태'] == '검정고시':
                    self.hwp.PutFieldText('검정고시', '■')


        except KeyError as e:
            print(f"필드 누락: {e}")
        except Exception as e:
            print(f"학력정보 입력 오류: {e}")
        
