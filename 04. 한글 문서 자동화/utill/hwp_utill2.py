import win32com.client as win32
import os

class HwpUtill:
    def __init__(self):
        try:
            self.hwp = win32.gencache.EnsureDispatch("hwpframe.hwpobject")
            self.hwp.RegisterModule("FilePathCheckDLL", "FilePathCheckerModuleExample")
            self.hwp.XHwpWindows.Item(0).Visible = True  # 한글 창을 보이게 설정
            print("Hwp COM object initialized successfully")
        except Exception as e:
            print(f"Failed to initialize Hwp COM object: {e}")
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
    
    def 세로누름틀생성(self, 시작인덱스, 필드이름, 개수):
        """
        세로로 텍스트를 삽입하여 필드처럼 보이게 처리.
        """
        try:
            for i in range(개수):
                field_name = f"{필드이름}_{시작인덱스 + i}"
                self.hwp.HAction.GetDefault("InsertText", self.hwp.HParameterSet.HInsertText)
                self.hwp.HParameterSet.HInsertText.Text = f"[{field_name}]"
                self.hwp.HAction.Execute("InsertText", self.hwp.HParameterSet.HInsertText)
                self.hwp.HAction.Run("MoveDown")  # 커서를 아래로 이동
        except Exception as e:
            print(f"Error creating vertical text fields: {e}")

    def 닫기(self):
        self.hwp.Clear(1)

    def 종료(self):
        self.hwp.Quit()
