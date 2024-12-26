from PyQt5.QtWidgets import QFileDialog, QLineEdit, QPushButton

class HwpPathComponent:
    def __init__(self, line_edit: QLineEdit, button: QPushButton):
        self.line_edit = line_edit
        self.button = button
        self.button.clicked.connect(self.add_hwp_path)

    def add_hwp_path(self):
        """한글 경로 추가 로직"""
        file_path, _ = QFileDialog.getOpenFileName(None, "한글 파일 선택", "", "HWP Files (*.hwp)")
        if file_path:
            self.line_edit.setText(file_path)
