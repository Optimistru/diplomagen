import typing

from common import models
from common import settings
from internal import db_controller


class DiplomaGenerator:
    def __init__(self, db: db_controller.DBManager):
        self.db = db

    def get_contestant_data(self, contestant_internal_name):
        contestant_name = self.db.get_contestant_full_name(contestant_internal_name)
        school_id = self.db.get_contestant_school_id(contestant_internal_name)
        school_name = self.db.get_school_name_by_id(school_id)
        return contestant_name, school_name

    def generate_diploma_data(self, score: models.Score) -> models.Diploma:
        diploma_settings = self.get_diploma_settings(score.problems_solved)
        contestant_name_raw, school_name_raw = self.get_contestant_data(score.contestant_internal_name)
        if not contestant_name_raw:
            print('ERROR: No contestant name for {}'.format(score.contestant_internal_name))
        if not school_name_raw:
            print('ERROR: No school name for {}'.format(score.contestant_internal_name))

        diploma = models.Diploma(
            degree=diploma_settings,
            contestant_full_name=self.get_contestant_name(contestant_name_raw),
            school_name=self.get_school_name(school_name_raw)
        )
        return diploma

    @staticmethod
    def get_diploma_settings(problems_solved):
        for item in settings.DIPLOMA_SETTINGS:
            if problems_solved >= item.problems_threshold:
                return item

    @staticmethod
    def get_contestant_name(full_name: typing.Optional[str]):
        if not full_name:
            contestant_name = settings.DEFAULT_NO_DATA
        else:
            full_name_list = full_name.split()
            if len(full_name_list) < 2:
                contestant_name = settings.DEFAULT_NO_DATA
            else:
                contestant_name = ' '.join(full_name_list[:2])
        return contestant_name

    @staticmethod
    def get_school_name(school_name: typing.Optional[str]):
        if not school_name:
            return settings.DEFAULT_NO_DATA
        return school_name.replace('&nbsp;', ' ')
