from dataclasses import dataclass
import typing


@dataclass
class Score:
    contestant_internal_name: str
    problems_solved: int
    penalty_sum: int

    def __repr__(self):
        return 'Name: <{}>, Solved: {}, Penalty: {}'.format(
            self.contestant_internal_name,
            self.problems_solved,
            self.penalty_sum
        )


@dataclass
class ProblemSolve:
    tries: int = 0
    penalty: int = 0
    success: bool = False

    def add_submit(self, success: bool, penalty: int):
        if self.success:
            return
        self.tries += 1
        self.penalty = penalty
        self.success = success


@dataclass
class Result:
    problems: typing.Dict[str, ProblemSolve]


@dataclass
class DiplomaDegree:
    degree_text: str
    status_text: str
    problems_threshold: int


@dataclass
class Diploma:
    degree: DiplomaDegree
    contestant_full_name: str
    school_name: str
