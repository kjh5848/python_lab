from PyQt5.QtWidgets import QComboBox
from Enum.program_step_enum import ProgramStep

class ComboComponent:
    def __init__(self, cmb_program_step: QComboBox, cmb_unit: QComboBox):
        self.cmb_program_step = cmb_program_step
        self.cmb_unit = cmb_unit

        # 초기 설정
        self.init_program_step()
        self.cmb_program_step.currentIndexChanged.connect(self.update_unit_options)

    def init_program_step(self):
        """초기화 시 프로그램 단계 콤보박스에 항목 추가"""
        self.cmb_program_step.clear()
        self.cmb_program_step.addItems([step.value for step in ProgramStep])
        self.cmb_unit.clear()

    def update_unit_options(self):
        """프로그램 단계 선택에 따라 단위 항목 변경"""
        selected_step_text = self.cmb_program_step.currentText()

        # Find the selected step in the Enum
        selected_step = next((step for step in ProgramStep if step.value == selected_step_text), None)

        # Update the unit ComboBox based on the selected step
        self.cmb_unit.clear()
        if selected_step:
            self.cmb_unit.addItems(selected_step.unit_options)
        else:
            self.cmb_unit.addItem("해당 없음")
