from app.core.kripke_model import KripkeModel
from app.core.harmonic_formula import ModalFormula
from app.core.formula_semantics import evaluate_formula
from app.schemas.request_response import AnalysisResult


def analyze_progression(chords: list) -> AnalysisResult:
    # Placeholder: hardcoded Kripke structure for example
    worlds = ["C", "G", "Am"]
    accessibility = {"C": ["G"], "G": ["Am"], "Am": []}
    labeling = {"C": chords, "G": chords, "Am": chords}
    model = KripkeModel(worlds, accessibility, labeling)
    formula = ModalFormula("tonal(C, [C, G, Am])")
    holds = evaluate_formula(model, ["C", "G", "Am"], formula)
    return AnalysisResult(
        tonic="C" if holds else "Ambiguous",
        explanation=f"Formula {formula.formula} evaluated to {holds}",
    )
