#%%
from utill import excel_utill, hwp_utill

# 파일 경로 및 시트 설정
EXCEL_FILE_PATH = r"C:\Users\Administrator\Desktop\미래내일일경험 공유\python_lab\07. 한글 문서\[광고마케팅] 241223 KTCA_30명.xlsx"
HWP_FILE_NAME = '[서식34] 인턴형 일경험 실시보고'
HWP_FILE_PATH = r"C:\Users\Administrator\Desktop\미래내일일경험 공유\python_lab\07. 한글 문서\★누름틀_문서\3. 사전직무 서류"
SAVE_FILE_PATH = r"C:\Users\Administrator\Desktop\미래내일일경험 공유\사전직무"

# 객체 생성
EObject = excel_utill.ExcelUtill()
HObject = hwp_utill.HwpUtill()


# 여러 시트 데이터 불러오기
sheet_names = ["참여자명단", "사전직무,운영기관,일경험 정보"]
excel_data = EObject.여러시트열기(EXCEL_FILE_PATH, sheet_names, header=0)


# 각 시트 데이터 가져오기
참여자명단 = excel_data["참여자명단"]
사전직무정보 = excel_data["사전직무,운영기관,일경험 정보"]


# 한글 파일 열기 및 필드 가져오기
field_names = HObject.필드가져오기(HWP_FILE_NAME, HWP_FILE_PATH)


HObject.홀짝필드채우기(사전직무정보,field_names)



field_mapping_group = {
        "성명": [f for f in field_names if f.startswith("성명_")],
        "생년월일": [f for f in field_names if f.startswith("생년월일_")],
        "성별": [f for f in field_names if f.startswith("성별_")],
        "연락처": [f for f in field_names if f.startswith("연락처_")],
        "프로그램명": [f for f in field_names if f.startswith("프로그램명_")]
}

fill_fields(
    hwp_object=HObject,
    data=참여자명단,
    field_mapping=field_mapping_group
)


# 결과 저장 및 닫기
HObject.저장(f"{HWP_FILE_NAME}_결과.hwp", SAVE_FILE_PATH)
HObject.닫기()
HObject.종료()
HObject.저장파일열기(SAVE_FILE_PATH)
# %%
