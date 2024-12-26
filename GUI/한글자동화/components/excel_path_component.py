from PyQt5.QtWidgets import QFileDialog, QLineEdit, QPushButton

class ExcelPathComponent:
    def __init__(self, line_edit: QLineEdit, button: QPushButton):
        self.line_edit = line_edit
        self.button = button
        self.button.clicked.connect(self.add_excel_path)

    def add_excel_path(self):
        """엑셀 경로 추가 로직"""
        file_path, _ = QFileDialog.getOpenFileName(None, "엑셀 파일 선택", "", "Excel Files (*.xls *.xlsx)")
        if file_path:
            self.line_edit.setText(file_path)
