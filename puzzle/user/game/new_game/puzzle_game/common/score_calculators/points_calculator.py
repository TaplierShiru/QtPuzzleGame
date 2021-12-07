

class PointsCalculator:

    POINTS_STEP = 5

    @staticmethod
    def update_score(bad_placed: int, max_placed: int) -> int:
        bad_score = bad_placed * PointsCalculator.POINTS_STEP
        max_score = max_placed * PointsCalculator.POINTS_STEP
        return max_score - bad_score

