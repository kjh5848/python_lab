#%%
from utill import excel_utill, hwp_utill

# 파일 경로 및 시트 설정
EXCEL_FILE_PATH = r"C:\Users\사용자\Desktop\미래내일일경험\python_lab\07. 한글 문서\[광고마케팅] 241223 KTCA_30명.xlsx"
HWP_FILE_NAME = '[서식13] 참여기업 지원금 지급 신청서'
HWP_FILE_PATH = r"C:\Users\사용자\Desktop\미래내일일경험\python_lab\07. 한글 문서\★누름틀_문서\5. 일경험 서류"
SAVE_FILE_PATH = r"C:\Users\사용자\Desktop\미래내일일경험\프로그램 운영"

# 객체 생성
EObject = excel_utill.ExcelUtill()
HObject = hwp_utill.HwpUtill()

# 여러 시트 데이터 불러오기
sheet_names = ["참여자명단", "사전직무,운영기관,일경험 정보"]
excel_data = EObject.여러시트열기(EXCEL_FILE_PATH, sheet_names, header=0)

field_names = HObject.필드가져오기(HWP_FILE_NAME, HWP_FILE_PATH)



# %%
