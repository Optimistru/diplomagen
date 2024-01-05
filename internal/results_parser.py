import abc
from collections import defaultdict
import typing
import json
from common import models, settings


class ParserManager:
    def __init__(self):
        self.s4ris = S4RISParser()

    def get_parser(self):
        if settings.PARSER == settings.PARSER_S4RIS:
            return self.s4ris
        else:
            raise NotImplementedError


class BaseParser(abc.ABC):
    @abc.abstractmethod
    def parse(self):
        pass


class S4RISParser(BaseParser):
    def parse(self):
        results: typing.Dict[str, models.Result] = dict()
        with open(settings.INPUT_FILENAME) as f:
            data = json.load(f)
        if not data:
            return results

        for contestant in data.get('contestants', []):
            results[contestant] = models.Result(problems=defaultdict(models.ProblemSolve))

        for run in data.get('runs', []):
            results[run['contestant']].problems[run['problemLetter']].add_submit(
                success=run['success'], penalty=int(run['timeMinutesFromStart'])
            )
        return results
