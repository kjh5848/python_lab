#%%
from utill import excel_utill, hwp_utill
import pandas as pd

def preprocess_education_data(data):
    """최종학력 데이터를 '고졸이하'와 '대학이상'으로 구분."""
    data['학력구분'] = data['최종학력구분'].apply(
        lambda x: '고졸이하' if x == '고등학교' else '대학이상'
    )
    return data

def 소계(data):
    """최종학력 데이터를 '고졸이하'와 '대학이상'으로 구분."""
    data['만족도참여'] = data['직무현황'].apply(
        lambda x: '수료' if x == '수료' else '미수료'
    )
    return data

def 포맷팅_비율(value):
    """소수점을 반올림하여 정수 비율로 반환"""
    return f"{round(value)}%" if not pd.isna(value) else "0%"

def calculate_and_fill_statistics(hwp_object, data, field_names):
    """성별, 연령별, 학력별, 지역별 통계를 계산하고 한글 문서의 누름틀에 채우기."""

    # 직무현황에서 "수료"인 데이터만 필터링
    filtered_data = data[data['직무현황'] == '수료']  # 직무현황이 "수료"인 행만 선택

    # 전체 인원수 계산
    total_count = len(filtered_data)

    # 성별 통계
    gender_counts = filtered_data['성별'].value_counts()
    gender_ratios = (gender_counts / total_count * 100).round(2)

    # 연령별 통계
    try:
        age_bins = [0, 20, 30, 40]
        age_labels = ['10대', '20대', '30대']
        filtered_data['연령대'] = pd.cut(filtered_data['만나이'].astype(int), bins=age_bins, labels=age_labels, right=False)
        age_counts = filtered_data['연령대'].value_counts().reindex(age_labels, fill_value=0)
        age_ratios = (age_counts / total_count * 100).round(2)
    except Exception as e:
        print(f"연령별 통계 계산 오류: {e}")
        return

    # 지역별 통계
    region_counts = filtered_data['지역'].value_counts()
    region_ratios = (region_counts / total_count * 100).round(2)

    # 학력별 통계
    try:
        education_data = preprocess_education_data(filtered_data)
        education_counts = education_data['학력구분'].value_counts()
        education_ratios = (education_counts / total_count * 100).round(2)
    except Exception as e:
        print(f"학력별 통계 계산 오류: {e}")
        return

    # 누름틀 필드 가져오기
    필드목록 = {
        "남": [field for field in field_names if field == "남"],
        "여": [field for field in field_names if field == "여"],
        "남%": [field for field in field_names if field == "남%"],
        "여%": [field for field in field_names if field == "여%"],
        "10대": [field for field in field_names if field == "10대"],
        "20대": [field for field in field_names if field == "20대"],
        "30대": [field for field in field_names if field == "30대"],
        "10대%": [field for field in field_names if field == "10대%"],
        "20대%": [field for field in field_names if field == "20대%"],
        "30대%": [field for field in field_names if field == "30대%"],
        "고졸이하": [field for field in field_names if field == "고졸이하"],
        "대학이상": [field for field in field_names if field == "대학이상"],
        "고졸%": [field for field in field_names if field == "고졸%"],
        "대학%": [field for field in field_names if field == "대학%"],
        "수도권": [field for field in field_names if field == "수도권"],
        "경상권": [field for field in field_names if field == "경상권"],
        "호남권": [field for field in field_names if field == "호남권"],
        "충청권": [field for field in field_names if field == "충청권"],
        "강원권": [field for field in field_names if field == "강원권"],
        "제주": [field for field in field_names if field == "제주"],
        "수도권%": [field for field in field_names if field == "수도권%"],
        "경상권%": [field for field in field_names if field == "경상권%"],
        "호남권%": [field for field in field_names if field == "호남권%"],
        "충청권%": [field for field in field_names if field == "충청권%"],
        "강원권%": [field for field in field_names if field == "강원권%"],
        "제주%": [field for field in field_names if field == "제주%"],
        "소계": [field for field in field_names if field == "소계"],
    }

    # 데이터 채우기
    try:
        # 성별 데이터
        if 필드목록["남"]:
            hwp_object.채우기(필드목록["남"][0], hwp_object._포맷팅(gender_counts.get("남", 0)))
        if 필드목록["남%"]:
            hwp_object.채우기(필드목록["남%"][0], f"{포맷팅_비율(gender_ratios.get('남', 0))}")
        if 필드목록["여"]:
            hwp_object.채우기(필드목록["여"][0], hwp_object._포맷팅(gender_counts.get("여", 0)))
        if 필드목록["여%"]:
            hwp_object.채우기(필드목록["여%"][0], f"{포맷팅_비율(gender_ratios.get('여', 0))}")

        # 연령대 데이터
        for age_label in age_labels:
            if 필드목록[age_label]:
                hwp_object.채우기(필드목록[age_label][0], hwp_object._포맷팅(age_counts.get(age_label, 0)))
            if 필드목록[f"{age_label}%"]:
                hwp_object.채우기(필드목록[f"{age_label}%"][0], f"{포맷팅_비율(age_ratios.get(age_label, 0))}")

        # 학력 데이터
        if 필드목록["고졸이하"]:
            hwp_object.채우기(필드목록["고졸이하"][0], hwp_object._포맷팅(education_counts.get("고졸이하", 0)))
        if 필드목록["고졸%"]:
            hwp_object.채우기(필드목록["고졸%"][0], f"{포맷팅_비율(education_ratios.get('고졸이하', 0))}")
        if 필드목록["대학이상"]:
            hwp_object.채우기(필드목록["대학이상"][0], hwp_object._포맷팅(education_counts.get("대학이상", 0)))
        if 필드목록["대학%"]:
            hwp_object.채우기(필드목록["대학%"][0], f"{포맷팅_비율(education_ratios.get('대학이상', 0))}")

        # 지역 데이터
        for region in ["수도권", "경상권", "호남권", "충청권", "강원권", "제주"]:
            if 필드목록[region]:
                hwp_object.채우기(필드목록[region][0], hwp_object._포맷팅(region_counts.get(region, 0)))
            if 필드목록[f"{region}%"]:
                hwp_object.채우기(필드목록[f"{region}%"][0], f"{포맷팅_비율(region_ratios.get(region, 0))}")

        # 소계 데이터
        if 필드목록["소계"]:
            hwp_object.채우기(필드목록["소계"][0], hwp_object._포맷팅(total_count))

    except Exception as e:
        print(f"오류 발생 (통계 채우기): {e}")


# 파일 경로 및 시트 설정
EXCEL_FILE_PATH = r"C:\Users\Administrator\Desktop\미래내일일경험 공유\python_lab\07. 한글 문서\[광고마케팅] 241223 KTCA_30명.xlsx"
HWP_FILE_NAME = "[서식129] (공통-직무교육기관) 사전직무교육 수료 보고서"
HWP_FILE_PATH = r'C:\Users\Administrator\Desktop\미래내일일경험 공유\python_lab\07. 한글 문서\★누름틀_문서\3. 사전직무 서류'
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
print(f"asdfsdfsdf{field_names}")

HObject.홀짝필드채우기(사전직무정보,field_names)

field_mapping_group = {
        "성명": [f for f in field_names if f.startswith("성명_")],
        "생년월일": [f for f in field_names if f.startswith("생년월일_")],
        "참여시간": [f for f in field_names if f.startswith("참여시간_")]
}

HObject.fill_fields(
    data=참여자명단,
    field_mapping=field_mapping_group
)


# 성별 통계 계산 및 채우기
calculate_and_fill_statistics(HObject, 참여자명단, field_names)

# 결과 저장 및 닫기
HObject.저장(f"{HWP_FILE_NAME}_결과.hwp", SAVE_FILE_PATH)
HObject.닫기()
HObject.종료()
HObject.저장파일열기(SAVE_FILE_PATH)

# %%
