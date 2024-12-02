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
    
    def 세로누름틀생성(hwp, 시작인덱스 , 필드이름, 개수):
        for i in range(개수):
            field_name = f"{필드이름}_{시작인덱스 + i}"
            
            # 누름틀 필드 생성 (현재 커서 위치에 삽입)
            hwp.CreateField(필드이름, "", field_name)
            print(f"Inserted field: {field_name}")
            hwp.HAction.Execute("MoveDown", hwp.HParameterSet.HFindReplace.HSet)

    def 닫기(self):
        self.hwp.Clear(1)

    def 종료(self):
        self.hwp.Quit()
    
    def 초기화(self,excel,select_row_index):
        
        for index, row in excel.iterrows():
            # A, B열 데이터 삽입
            self.hwp.PutFieldText(select_row_index,"")  # A열: 필드명, B열: 값
             
