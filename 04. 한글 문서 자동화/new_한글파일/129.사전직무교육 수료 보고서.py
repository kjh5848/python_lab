#%%
from utill import excel_utill, hwp_utill

# 파일 경로 및 시트 설정
EXCEL_FILE_PATH = r"C:\Users\Administrator\Desktop\미래내일일경험 공유\python_lab\07. 한글 문서\[광고마케팅] 241223 KTCA_30명.xlsx"
HWP_FILE_NAME = "[서식129] (공통-직무교육기관) 사전직무교육 수료 보고서"
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


for row_index, row_data in 사전직무정보.iterrows():
    try:
        # 열 순회: 모든 열에서 필드명, 값 쌍으로 처리
        for col_index in range(1, len(row_data), 2):  # 2칸씩 건너뛰기 (필드명, 값 쌍)
            field_name = row_data[col_index]  # 현재 열 (필드명)
            if col_index + 1 < len(row_data):  # 값 열이 존재하는지 확인
                field_value = row_data[col_index + 1]
            else:
                continue  # 값 열이 없으면 스킵

            # 필드 이름이 한글 필드 목록에 있는 경우만 처리
            if field_name in field_names:
                HObject.채우기(field_name, str(field_value))

    except Exception as e:
        print(f"오류 발생 (사전직무정보 행: {row_index + 1}, 열: {col_index}): {e}")


# 프로그램별 참여자 수를 구하기
grouped = 참여자명단.groupby(["프로그램명","직무","운영기관명"])



# 참여자명단 데이터를 누름틀에 채우기
성명_필드목록 = [field for field in field_names if field.startswith("성명_")]
생년월일_필드목록 = [field for field in field_names if field.startswith("생년월일_")]
참여시간_필드목록 = [field for field in field_names if field.startswith("참여시간_")]
 

for index, row in 참여자명단.iterrows():
    try:
        성명_필드 = f"성명_{index + 1}"
        생년월일_필드 = f"생년월일_{index + 1}"
        참여시간_필드 = f"참여시간_{index + 1}"

        if 성명_필드 in 성명_필드목록:
            HObject.채우기(성명_필드, row['성명'])
        if 생년월일_필드 in 생년월일_필드목록:
            HObject.채우기(생년월일_필드, row['생년월일'])
        if 참여시간_필드 in 참여시간_필드목록:
            HObject.채우기(참여시간_필드, row['참여시간'])
    except Exception as e:
        print(f"오류 발생 (참여자명단 행: {index + 1}): {e}")


# 결과 저장 및 닫기
HObject.저장(f"{HWP_FILE_NAME}_결과.hwp", SAVE_FILE_PATH)
HObject.닫기()
HObject.종료()
HObject.저장파일열기(SAVE_FILE_PATH)

# %%
