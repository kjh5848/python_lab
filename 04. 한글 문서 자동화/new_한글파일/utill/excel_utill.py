#%%
import pandas as pd

class ExcelUtill:
    # @staticmethod
    # def 엑셀열기(file_path_excel, sheet_name, header):
    #     excel = pd.read_excel(file_path_excel, sheet_name=sheet_name, header=header, dtype=str)
    #     excel_data = excel.fillna("")
    #     return excel_data

    @staticmethod
    def 엑셀열기(file_path_excel, sheet_name=None, header=0):
        """
        엑셀 파일에서 시트를 읽어오는 메서드
        :param file_path_excel: 엑셀 파일 경로
        :param sheet_name: 시트 이름 (None일 경우 전체 시트 로드)
        :param header: 헤더 행 번호
        :return: DataFrame 또는 {시트 이름: DataFrame} 딕셔너리
        """
        if sheet_name is None:
            # 시트 이름이 지정되지 않으면 모든 시트를 불러옴
            return pd.read_excel(file_path_excel, sheet_name=None, header=header, dtype=str).fillna("")
        else:
            # 특정 시트를 불러옴
            return pd.read_excel(file_path_excel, sheet_name=sheet_name, header=header, dtype=str).fillna("")

    @staticmethod
    def 여러시트열기(file_path_excel, sheet_names, header=0):
        """
        여러 시트를 불러오는 메서드
        :param file_path_excel: 엑셀 파일 경로
        :param sheet_names: 불러올 시트 이름 리스트
        :param header: 헤더 행 번호
        :return: {시트 이름: DataFrame} 딕셔너리
        """
        excel_data = {}
        for sheet_name in sheet_names:
            excel_data[sheet_name] = ExcelUtill.엑셀열기(file_path_excel, sheet_name, header)
        return excel_data