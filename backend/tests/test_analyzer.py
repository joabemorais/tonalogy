from app.core.analyzer import analyze_progression


def test_basic_progression():
    chords = ["C", "G", "Am", "F"]
    result = analyze_progression(chords)
    assert result.tonic == "C"
    assert "evaluated to True" in result.explanation
