from fastapi import APIRouter
from app.schemas.request_response import AnalysisRequest, AnalysisResult
from app.core.analyzer import analyze_progression

router = APIRouter()


@router.post("/analyze", response_model=AnalysisResult)
def analyze(input_data: AnalysisRequest):
    return analyze_progression(input_data.chords)
