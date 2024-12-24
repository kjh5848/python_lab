import tkinter as tk
from tkinter import ttk, filedialog
from excel_service import ExcelService
from 서식관리자.서식모음 import 서식이름, 서식모음
import os

class DocumentAutomationApp:
    def __init__(self, root):
        self.excel_service = ExcelService()
        self.서식들 = 서식모음()

        self.root = root
        self.root.title("한글 서식 자동화 도구")
        self.root.geometry("500x400")
        
        # 엑셀 파일 경로 변수와 라벨
        self.excel_file_path = tk.StringVar()
        self.excel_label = tk.Label(root, text="엑셀 파일 경로:")
        self.excel_label.pack(pady=10)
        self.excel_entry = tk.Entry(root, textvariable=self.excel_file_path, width=50)
        self.excel_entry.pack(pady=5)
        

        # 엑셀 파일 선택 버튼
        self.excel_button = tk.Button(root, text="엑셀 파일 선택", command=self.select_excel_file)
        self.excel_button.pack(pady=5)
        
        # 서식 파일 경로 변수와 라벨
        self.form_file_path = tk.StringVar()
        self.form_label = tk.Label(root, text="서식 파일 경로:")
        self.form_label.pack(pady=5)
        self.form_entry = tk.Entry(root, textvariable=self.form_file_path, width=50)
        self.form_entry.pack(pady=5)
        
        # 서식 파일 선택 버튼
        self.form_button = tk.Button(root, text="서식 파일 선택", command=self.select_form_file)
        self.form_button.pack(pady=5)
        
        # 드롭다운 메뉴로 서식 선택
        self.form_types = [
            "[서식33] 인턴형 일경험 참여신청서",
            "[서식46] 인턴형 참여청년 확인서",
            ]
        self.form_selection = ttk.Combobox(root, values=self.form_types)
        self.form_selection.set("서식을 선택하세요")
        self.form_selection.pack(pady=10)
        
        # 실행 버튼
        self.execute_button = tk.Button(root, text="실행", command=self.execute)
        self.execute_button.pack(pady=20)

    def select_excel_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
        self.excel_file_path.set(file_path)

    def select_form_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("HWP files", "*.hwp")])
        self.form_file_path.set(file_path)

    def execute(self):
        excel_path = self.excel_file_path.get()
        form_path = self.form_file_path.get()
        selected_form = self.form_selection.get()

        if not excel_path or not form_path or selected_form == "서식을 선택하세요":
            print("모든 필드를 올바르게 선택하세요.")
            return
            
        # Enum을 사용하여 드롭다운 값과 서식 키를 맞추기
        try:
            서식명 = 서식이름(selected_form).value
            self.서식들.실행(서식명, excel_path, form_path)
        except ValueError:
            print("지원하지 않는 서식입니다.")
