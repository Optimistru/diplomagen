import json

import mysql.connector


class DBController:
    def __enter__(self):
        with open('secdist.json') as secdist:
            try:
                db_settings = json.load(secdist)
            except json.JSONDecodeError:
                print('ERROR: JSON decode error')
                raise

        try:
            self.connection = mysql.connector.connect(
                host=db_settings['host'],
                port=db_settings['port'],
                user=db_settings['user'],
                password=db_settings['password'],
                database=db_settings['db_name'],
            )
        except KeyError:
            print('ERROR: Not enough keys in secdist file')
            raise

        self.cursor = self.connection.cursor()
        return self

    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchone()
        except mysql.connector.Error as err:
            print(f'ERROR: {str(err)}')
            return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.connection.close()


class DBManager:
    def __init__(self, db: DBController):
        self.db = db

    def get_school_name_by_id(self, school_id: int):
        if not school_id:
            return None
        data = self.db.execute_query(
            f'SELECT name FROM personal_ivt.c_schools WHERE id={int(school_id)};'
        )
        return data[0] if data else None

    def get_contestant_full_name(self, user_name):
        if not user_name:
            return None
        data = self.db.execute_query(
            f'SELECT fullname FROM personal_ivt.c_users WHERE name=\'{user_name}\';'
        )
        return data[0] if data else None

    def get_contestant_school_id(self, user_name):
        if not user_name:
            return None
        data = self.db.execute_query(
            f'SELECT idSchool FROM personal_ivt.c_users WHERE name=\'{user_name}\';'
        )
        return data[0] if data else None
