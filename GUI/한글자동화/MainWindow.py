from qt_imports import *
from components.components_init import *

# UI 파일 경로
ui_path = os.path.join(os.path.dirname(__file__), "한글자동화.ui")
form_class = uic.loadUiType(ui_path)[0]

class MainWindow(QMainWindow,form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 콤보박스 컴포넌트 초기화
        self.combo_component = ComboComponent(
            cmb_program_step = self.program_cmb1,
            cmb_unit = self.program_cmb2
            )
        
         # ExcelPathComponent 초기화
        self.excel_path_component = ExcelPathComponent(
            line_edit=self.excel_path_line_edit,  # UI에서 가져온 엑셀 경로 라인 에디트
            button=self.excel_add_button  # UI에서 가져온 엑셀 경로 추가 버튼
        )

        # HwpPathComponent 초기화
        self.hwp_path_component = HwpPathComponent(
            line_edit=self.hwp_path_line_edit,  # UI에서 가져온 한글 경로 라인 에디트
            button=self.hwp_add_button  # UI에서 가져온 한글 경로 추가 버튼
        )