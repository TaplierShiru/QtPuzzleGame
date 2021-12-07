from puzzle.utils import SCORE_TIME, SCORE_POINTS

from .points_calculator import PointsCalculator


class ScoreCalculatorController:

    def __init__(self, type_score: str):
        self._type_score = type_score

    def update_score(
            self, bad_placed: int, max_placed: int,
            start_time: int, current_time: int) -> int:
        if self._type_score == SCORE_TIME:
            return start_time + current_time
        elif self._type_score == SCORE_POINTS:
            return PointsCalculator.update_score(bad_placed=bad_placed, max_placed=max_placed)

