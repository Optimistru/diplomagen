from common import models

DEFAULT_MISTAKE_PENALTY = 20

PARSER_S4RIS = 'S4RIS'
PARSER = PARSER_S4RIS

SEASON = 'Весна-2023'
D1, D2, D3 = (6, 5, 4)

INPUT_FILENAME = 'input.txt'
RESULT_FILENAME = '{}.docx'.format(SEASON)

SIGN_ULIVT = 'Председатель оргкомитета чемпионата\nд.т.н., профессор кафедры ВТ УлГТУ\tВ.Н.Негода'
SIGN_DEAN = 'Декан ФИСТ УЛГТУ\tК.В.Святов'

DIPLOMA_SETTINGS = [
    models.DiplomaDegree(
        problems_threshold=D1,
        degree_text='I степени',
        status_text='победитель',
    ),
    models.DiplomaDegree(
        problems_threshold=D2,
        degree_text='II степени',
        status_text='победитель',
    ),
    models.DiplomaDegree(
        problems_threshold=D3,
        degree_text='III степени',
        status_text='призер',
    ),
    models.DiplomaDegree(
        problems_threshold=0,
        degree_text='',
        status_text='участник',
    ),
]

DEFAULT_NO_DATA = 'NO DATA'
