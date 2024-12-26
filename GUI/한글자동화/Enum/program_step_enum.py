from enum import Enum

# Define program steps as Enum
class ProgramStep(Enum):
    SELECT = "선택"
    BUSINESS = "기업서류"
    YOUTH = "청년서류"
    REGISTER = "프로그램 등록"
    PRE_JOB = "사전직무운영"
    EXPERIENCE = "일경험 운영"
    TERMINATION = "일경험 종료"

# Map program steps to unit options
UNIT_OPTIONS = {
    ProgramStep.SELECT: [],
    ProgramStep.BUSINESS: [],
    ProgramStep.YOUTH: [],
    ProgramStep.REGISTER: ["등록 단위 1", "등록 단위 2", "등록 단위 3"],
    ProgramStep.PRE_JOB: ["사전직무 단위 1", "사전직무 단위 2"],
    ProgramStep.EXPERIENCE: ["운영 단위 1", "운영 단위 2", "운영 단위 3", "운영 단위 4"],
    ProgramStep.TERMINATION: ["종료 단위 1", "종료 단위 2"],
}
