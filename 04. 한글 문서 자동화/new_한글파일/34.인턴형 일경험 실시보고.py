#%%
from utill import excel_utill, hwp_utill


def 프로그램목록(HObject,field_names,excel_sheet):

    grouped = excel_sheet.groupby(["프로그램명","직무","운영기관명"])
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
    
    

def fill_fields(hwp_object, data, field_mapping):
    """시작하는 필드 이름을 동적으로 매핑하여 데이터를 채우기."""
    for index, row in data.iterrows():
        try:
            for excel_col, hwp_fields in field_mapping.items():
                if index < len(hwp_fields):
                    hwp_field_name = hwp_fields[index]
                    hwp_object.채우기(hwp_field_name, row[excel_col])
        except Exception as e:
            print(f"오류 발생 (행: {index + 1}, 필드: {excel_col}): {e}")


# 파일 경로 및 시트 설정
EXCEL_FILE_PATH = r"C:\Users\사용자\Desktop\미래내일일경험\python_lab\07. 한글 문서\[광고마케팅] 241223 KTCA_30명.xlsx"
HWP_FILE_NAME = '[서식34] 인턴형 일경험 실시보고'
HWP_FILE_PATH = r"C:\Users\사용자\Desktop\미래내일일경험\python_lab\07. 한글 문서\★누름틀_문서\3. 사전직무 서류"
SAVE_FILE_PATH = r"C:\Users\사용자\Desktop\미래내일일경험\사전직무"

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


프로그램목록(
    field_names=field_names,
    HObject=HObject,
    excel_sheet=참여자명단
)


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
