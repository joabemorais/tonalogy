from pydantic import BaseModel
from typing import List


class AnalysisRequest(BaseModel):
    chords: List[str]


class AnalysisResult(BaseModel):
    is_tonal: bool
    explanations: List[str]
