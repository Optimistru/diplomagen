import typing
from common import models
from common import settings


class ScoreCalculator:

    def calculate_score(self, results: typing.Dict[str, models.Result]):
        data: typing.List[models.Score] = []
        for contestant, result in results.items():
            data.append(
                models.Score(
                    contestant_internal_name=contestant,
                    problems_solved=self._calculate_problems_solved(result),
                    penalty_sum=self._calculate_penalty_sum(result)
                )
            )

        data.sort(key=lambda x: (-x.problems_solved, x.penalty_sum, x.contestant_internal_name))
        return data

    @staticmethod
    def _calculate_penalty_sum(results: models.Result):
        return sum(
            (result.tries - 1) * settings.DEFAULT_MISTAKE_PENALTY + result.penalty
            for _, result in results.problems.items()
            if result.success
        )

    @staticmethod
    def _calculate_problems_solved(results: models.Result):
        return sum(1 for _, result in results.problems.items() if result.success)
