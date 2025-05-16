from typing import List


class ModalFormula:
    def __init__(self, formula: str):
        self.formula = formula

    def __repr__(self):
        return f"Formula({self.formula})"
