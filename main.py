from internal import db_controller
from internal.results_parser import ParserManager
from internal.score_calculator import ScoreCalculator
from internal.diploma_generator import DiplomaGenerator
from output.text_document import TextDocument


def main():
    contest_results = ParserManager().get_parser().parse()
    print('Parsed contest results')
    scores = ScoreCalculator().calculate_score(contest_results)
    print(f'Got contest scores: {scores}')
    with db_controller.DBController() as db_conn:
        db = db_controller.DBManager(db_conn)
        diploma_generator = DiplomaGenerator(db)
        diplomas = [diploma_generator.generate_diploma_data(score) for score in scores]
    print('Generated diploma data')
    doc_generator = TextDocument()
    doc_generator.generate(diplomas)
    print(f'Generated {len(diplomas)} diplomas in file {doc_generator.filename}')


if __name__ == '__main__':
    main()
