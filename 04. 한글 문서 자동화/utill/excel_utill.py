import pandas as pd

class ExcelUtill:
    @staticmethod
    def 엑셀열기(file_path_excel, sheet_name, header):
        excel = pd.read_excel(file_path_excel, sheet_name=sheet_name, header=header, dtype=str)
        excel_data = excel.fillna("")
        return excel_data
