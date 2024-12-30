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
program_counts = grouped.size()


# 필요한 필드 수 계산
필요한필드수 = len(program_counts)
프로그램프로젝트명 = [field for field in field_names if field.startswith("프로그램프로젝트명")][:필요한필드수]
참여인원 = [field for field in field_names if field.startswith("참여인원")][:필요한필드수]
직무필드목록 = [field for field in field_names if field.startswith("직무")][:필요한필드수]
운영기관명필드목록 = [field for field in field_names if field.startswith("운영기관명")][:필요한필드수]


# 그룹화된 데이터를 리스트로 변환
grouped_keys = list(grouped.groups.keys())


# 프로그램별 정보를 필드에 채우기
for i, ((program_name, job_role, institution_name), count) in enumerate(program_counts.items()):
    try:
        if i >= len(프로그램프로젝트명) or i >= len(참여인원) or i >= len(직무필드목록) or i >= len(운영기관명필드목록):
            print(f"누름틀 부족: 프로그램 '{program_name}', 직무 '{job_role}', 운영기관명 '{institution_name}'")
            break

        # 필드 이름 매칭
        프로그램필드 = 프로그램프로젝트명[i]
        인원필드 = 참여인원[i]
        직무필드 = 직무필드목록[i]
        운영기관명필드 = 운영기관명필드목록[i]

        # 데이터 삽입
        HObject.채우기(프로그램필드, program_name)       # 프로그램명 삽입
        HObject.채우기(직무필드, job_role)              # 직무 삽입
        HObject.채우기(운영기관명필드, institution_name) # 운영기관명 삽입
        HObject.채우기(인원필드, str(count))            # 참여인원 삽입
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
HObject.종료()
HObject.저장파일열기(SAVE_FILE_PATH)

# %%
