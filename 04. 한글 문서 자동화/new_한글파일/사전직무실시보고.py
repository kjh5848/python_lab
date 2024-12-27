#%%
from utill import excel_utill, hwp_utill

# 파일 경로 및 시트 설정
EXCEL_FILE_PATH = r"C:\Users\Administrator\Desktop\미래내일일경험 공유\python_lab\07. 한글 문서\[광고마케팅] 241223 KTCA_30명.xlsx"
HWP_FILE_NAME = "[서식125] (공통직무교육기관) 사전직무교육 실시보고"
HWP_FILE_PATH = r"C:\Users\Administrator\Desktop\미래내일일경험 공유\python_lab\07. 한글 문서\★누름틀_문서\3. 사전직무 서류"
SAVE_FILE_PATH = r"C:\Users\Administrator\Desktop\미래내일일경험 공유\사전직무"

# 객체 생성
EObject = excel_utill.ExcelUtill()
HObject = hwp_utill.HwpUtill()

# 여러 시트 데이터 불러오기
sheet_names = ["참여자명단", "사전직무"]
excel_data = EObject.여러시트열기(EXCEL_FILE_PATH, sheet_names, header=0)

# 각 시트 데이터 가져오기
참여자명단 = excel_data["참여자명단"]
사전직무정보 = excel_data["사전직무"]

# 한글 파일 열기 및 필드 가져오기
field_names = HObject.필드가져오기(HWP_FILE_NAME, HWP_FILE_PATH)

# 사전직무정보 데이터를 한글 문서에 채우기
for index, row in 사전직무정보.iterrows():
    try:
        field_name = row[1]  # B열: 필드명
        field_value = row[2]  # C열: 값

        if field_name in field_names:
            HObject.채우기(field_name, str(field_value))
    except Exception as e:
        print(f"오류 발생 (사전직무정보 행: {index + 1}): {e}")

# 프로그램별 참여자 수를 구하기
grouped = 참여자명단.groupby("프로그램명")
program_counts = grouped.size()

# 필요한 필드 수 계산
필요한필드수 = len(program_counts)
프로그램프로젝트명 = [field for field in field_names if field.startswith("프로그램프로젝트명")][:필요한필드수]
참여인원 = [field for field in field_names if field.startswith("참여인원")][:필요한필드수]

# 프로그램별 정보를 필드에 채우기
for i, (program_name, count) in enumerate(program_counts.items()):
    try:
        if i >= len(프로그램프로젝트명) or i >= len(참여인원):
            print(f"누름틀 부족: 프로그램 '{program_name}', 인원 {count}명")
            break

        프로그램필드 = 프로그램프로젝트명[i]
        인원필드 = 참여인원[i]

        HObject.채우기(프로그램필드, program_name)
        HObject.채우기(인원필드, str(count))
    except Exception as e:
        print(f"오류 발생 (프로그램: {program_name}): {e}")

# 참여자명단 데이터를 누름틀에 채우기
성명_필드목록 = [field for field in field_names if field.startswith("성명_")]
생년월일_필드목록 = [field for field in field_names if field.startswith("생년월일_")]
성별_필드목록 = [field for field in field_names if field.startswith("성별_")]
연락처_필드목록 = [field for field in field_names if field.startswith("연락처_")]
프로그램명_필드목록 = [field for field in field_names if field.startswith("프로그램명_")]

for index, row in 참여자명단.iterrows():
    try:
        성명_필드 = f"성명_{index + 1}"
        생년월일_필드 = f"생년월일_{index + 1}"
        성별_필드 = f"성별_{index + 1}"
        연락처_필드 = f"연락처_{index + 1}"
        프로그램명_필드 = f"프로그램명_{index + 1}"

        if 성명_필드 in 성명_필드목록:
            HObject.채우기(성명_필드, row['성명'])
        if 생년월일_필드 in 생년월일_필드목록:
            HObject.채우기(생년월일_필드, row['생년월일'])
        if 성별_필드 in 성별_필드목록:
            HObject.채우기(성별_필드, row['성별'])
        if 연락처_필드 in 연락처_필드목록:
            HObject.채우기(연락처_필드, row['연락처'])
        if 프로그램명_필드 in 프로그램명_필드목록:
            HObject.채우기(프로그램명_필드, row['프로그램명'])
    except Exception as e:
        print(f"오류 발생 (참여자명단 행: {index + 1}): {e}")

# 결과 저장 및 닫기
HObject.저장(f"{HWP_FILE_NAME}_결과.hwp", SAVE_FILE_PATH)
HObject.닫기()
HObject.저장파일열기(SAVE_FILE_PATH)
