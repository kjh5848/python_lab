#%%

from openai import OpenAI
from utill import excel_utill, hwp_utill

# 파일 경로 및 시트 설정
EXCEL_FILE_PATH = r"C:\Users\Administrator\Desktop\미래내일일경험 공유\python_lab\07. 한글 문서\[쇼우테크] SNS콘텐츠 마케팅 인턴십.xlsx"
HWP_FILE_NAME = "[서식 109] 인턴형 일경험 종합 보고서 KTCA"
HWP_FILE_PATH = r"C:\Users\Administrator\Desktop\미래내일일경험 공유\python_lab\07. 한글 문서\★누름틀_문서\5. 일경험 서류"
SAVE_FILE_PATH = r"C:\Users\Administrator\Desktop\미래내일일경험 공유\KTCA종합보고서"

# 객체 생성
EObject = excel_utill.ExcelUtill()
HObject = hwp_utill.HwpUtill()

# 여러 시트 데이터 불러오기
sheet_names = ["참여자명단"]
excel_data = EObject.여러시트열기(EXCEL_FILE_PATH, sheet_names, header=0)
# 각 시트 데이터 가져오기
참여자명단 = excel_data["참여자명단"]

def 한글문서생성(HObject, excel_data, hwp_file_name, hwp_file_path, save_file_path):
    """엑셀 데이터를 기반으로 한글 문서를 생성"""
    # 한글 파일에서 필드 이름 가져오기
    field_names = HObject.필드가져오기(hwp_file_name, hwp_file_path)

    for _, row in excel_data.iterrows():
        try:
            # 한글 파일 열기
            HObject.파일열기(hwp_file_name, hwp_file_path)
            # 필드 채우기
            HObject.필드채우기(field_names, row)
            
    # 저장 경로 확인 및 저장
            HObject.저장폴더(save_file_path)
            new_file_name = f"{hwp_file_name}_{row['성명']}.hwp"
            HObject.저장(new_file_name, save_file_path)

            print(f"파일 생성 완료: {new_file_name}")
        except Exception as e:
            print(f"오류 발생 (성명: {row['성명']}): {e}")
        finally:
            # 한글 파일 닫기
            HObject.닫기()

    # 저장된 파일 폴더 열기
    HObject.저장파일열기(save_file_path)

    # 한글 종료
    HObject.종료()

        
한글문서생성(
    HObject=HObject,
    excel_data=excel_data["참여자명단"],
    hwp_file_name=HWP_FILE_NAME,
    hwp_file_path=HWP_FILE_PATH,
    save_file_path=SAVE_FILE_PATH
)
            


# # %%

# %%
