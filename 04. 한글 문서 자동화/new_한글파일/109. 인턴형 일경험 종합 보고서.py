#%%

from openai import OpenAI
from utill import excel_utill, hwp_utill

# 파일 경로 및 시트 설정
EXCEL_FILE_PATH = r"C:\Users\사용자\Desktop\미래내일일경험\python_lab\07. 한글 문서\[광고마케팅] 241223 KTCA_30명.xlsx"
HWP_FILE_NAME = '[서식109] (인턴형-참여청년) 인턴형 일경험 종합 보고서'
HWP_FILE_PATH = r"C:\Users\사용자\OneDrive\한국융합인재교육협회\요청파일\19명"
SAVE_FILE_PATH = r"C:\Users\사용자\OneDrive\한국융합인재교육협회\요청파일\19명"

# 객체 생성
EObject = excel_utill.ExcelUtill()
HObject = hwp_utill.HwpUtill()

# 여러 시트 데이터 불러오기
sheet_names = ["참여자명단", "사전직무,운영기관,일경험 정보"]
try:
    excel_data = EObject.여러시트열기(EXCEL_FILE_PATH, sheet_names, header=0)
    field_names = HObject.필드가져오기(HWP_FILE_NAME, HWP_FILE_PATH)
except Exception as e:
    print(f"오류 발생: {e}")
    exit()

# OpenAI 클라이언트 초기화
# client = OpenAI(api_key="")

# 시스템 메시지 정의
sys_content = """
너는 미래내일일경험의 운영기관 담당자야 학생의 수와 진행하는 프로젝트에 맞춰서 종합보고서를 만들어야해 제공되는 정보는 프로젝트명이고 아래 예시대로 종합보고서를 작성해줘
⬛ {week}주차 프로젝트\n
삼경정기 주요제품, 고객사 파악\n
⬛ 프로젝트 진행현황\n
삼경정기의 주요 제품 종류와 특징을 정리하고 관련 자료를 확인했습니다.\n
⬛ 느낀점\n
처음에는 제품과 고객사를 이해하는 게 조금 복잡했는데, 자료를 정리하면서 점점 흐름이 잡힌 느낌이고, 삼경정기가 다양한 산업에서 중요한 역할을 하고 있다는 걸 알게 됐습니다.\n

아래 요건을 검토하세요.
프로젝트 진행형황
1. 간단하게 2개의 현황 작성

느낀점은 
1. ~요, ~다 쓰지않기
2. 느낀점 중간에 '~다' 로 끝나지 말고 '고', '습니다'
3. 너무 ai 스럽지 않게 너무 전문적이지 않은 톤으로 20대 초반의 대학생느낌

주의사항 위 예시와 동일하게 한글파일에 줄바꿈이 가능하도록 출력을 맞춰주세요.
"""


# 프로젝트 정의
project_descriptions = [
    {"주차": "1주차", "내용": "각 직무별 담당 업무 파악"},
    {"주차": "2주차", "내용": "부서 업무 프로세스, 보고 체계 이해"},
    {"주차": "3주차", "내용": "부서 업무 프로세스, 보고 체계 이해"},
    {"주차": "4주차", "내용": "주간 업무보고서 및 내부품의서 작성"},
    {"주차": "5주차", "내용": "주간 업무보고서 및 내부품의서 작성"},
    {"주차": "6주차", "내용": "부서별 회의 준비 및 회의록 작성 방법 파악"},
    {"주차": "7주차", "내용": "부서별 회의 준비 및 회의록 작성 방법 파악"},
    {"주차": "8주차", "내용": "월 성과보고서 작성 보조"},
    {"주차": "9주차", "내용": "월 성과보고서 작성 보조"},
    {"주차": "10주차", "내용": "주간 업무보고서 및 내부품의서 작성"},
    {"주차": "11주차", "내용": "주간 업무보고서 및 내부품의서 작성"},
    {"주차": "12주차", "내용": "인턴 활동 결과보고서 작성 및 담당자 피드백 체크"}
]
# GPT-4 API 호출 함수
def generate_report_content(project_description):
    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": sys_content},
                {"role": "user", "content": f"⬛ {project_description['주차']} 프로젝트\n{project_description['내용']}"},
            ],
            model="gpt-4o-2024-05-13",
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"GPT-4 API 호출 중 오류 발생: {e}")
        return "오류 발생: 내용을 생성할 수 없습니다."


# 소감 메시지 정의
summary_prompt = """
프로젝트에 맞춰 느낀 개인적 성장과 경험을 바탕으로 작성해주고 너무 전문적이지 않게 소감을 작성하라.
1. 너무 길지 않게 4문장으로 작성
3. 주체는 참여한 학생의 기준으로 작성
4. '~요', '~다'쓰지않기 반말하지 않기
5. 느낀점 중간에 '~다' 로 끝나지 말고 '고', '습니다'로 이어갈 수 있게 작성
6. 너무 ai 스럽지 않게 너무 전문적이지 않은 톤으로 20대 초반의 예의 바른 대학생느낌
"""

# 소감 생성 함수
def generate_summary(weeks, projects):
    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": summary_prompt.format(weeks=weeks, projects=projects)}
            ],
            model="gpt-4o-2024-05-13",
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"소감 생성 중 오류 발생: {e}")
        return "오류 발생: 소감을 생성할 수 없습니다."

# 데이터 생성 로직
num_participants = 8  # 참여자 수
num_weeks = 12  # 주차 수
final_reports = {}

for participant in range(1, num_participants + 1):
    participant_reports = {}
    for week in range(1, num_weeks + 1):
        participant_reports[f"{week}주차"] = generate_report_content(project_descriptions[week-1])

    summary = generate_summary(num_weeks, ", ".join([p["내용"] for p in project_descriptions]))
    participant_reports["소감"] = summary
    final_reports[f"{participant}"] = participant_reports

# 생성된 데이터 확인 (옵션)
for participant, reports in final_reports.items():
    print(f"{participant}의 보고서:")
    for key, value in reports.items():
        print(f"{key}: {value}")
    print("=" * 50)

# HWP 필드에 데이터 매칭 및 저장
try:
    for participant, reports in final_reports.items():
        fields = HObject.필드가져오기(HWP_FILE_NAME, HWP_FILE_PATH)  # HWP 파일에 정의된 필드 목록 가져오기
        for field_name, content in reports.items():
            if field_name in fields:
                HObject.채우기(field_name, content)
            else:
                print(f"Field '{field_name}' not found in the document.")

        # 파일 저장
        HObject.저장폴더(SAVE_FILE_PATH)
        new_file_name = f"{HWP_FILE_NAME}_{participant}.hwp"
        HObject.저장(new_file_name, SAVE_FILE_PATH)
        print(f"파일이 성공적으로 저장되었습니다: {SAVE_FILE_PATH}/{new_file_name}")
        # 한글 파일 닫기
        HObject.닫기()
except Exception as e:
    print(f"HWP 파일 처리 중 오류 발생: {e}")
finally:
    # 저장된 파일 폴더 열기
    HObject.저장파일열기(SAVE_FILE_PATH)
    HObject.종료()




# %%
