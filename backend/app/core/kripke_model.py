from typing import Dict, List


class KripkeModel:
    def __init__(
        self,
        worlds: List[str],
        accessibility: Dict[str, List[str]],
        labeling: Dict[str, List[str]],
    ):
        self.worlds = worlds  # tonal centers (e.g., C, G, Am)
        self.accessibility = accessibility  # modulations
        self.labeling = labeling  # labels for each world (chords)
