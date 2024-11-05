import pandas as pd

class ExcelService:
    @staticmethod
    def 엑셀열기(file_path_excel, sheet_name):
        excel = pd.read_excel(file_path_excel, sheet_name=sheet_name, header=1, dtype=str)
        excel_data = excel.fillna("")
        return excel_data
