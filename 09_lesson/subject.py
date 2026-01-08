from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError


class SubjectTable:
    def __init__(self, connection_string):
        self.engine = create_engine(connection_string)

    def create_subject(self, subject_id, subject_title):
        try:
            with self.engine.begin() as conn:
                conn.execute(
                    text("INSERT INTO subject (\"subject_id\", \"subject_title\") VALUES (:id, :title)"),
                    {"id": subject_id, "title": subject_title}
                )
        except SQLAlchemyError as e:
            print(f"An error occurred during subject creation: {e}")

    def update_subject(self, subject_id, new_title):
        try:
            with self.engine.begin() as conn:
                conn.execute(
                    text("UPDATE subject SET \"subject_title\" = :title WHERE \"subject_id\" = :id"),
                    {"id": subject_id, "title": new_title}
                )
        except SQLAlchemyError as e:
            print(f"An error occurred during subject update: {e}")

    def delete_subject(self, subject_id):
        try:
            with self.engine.begin() as conn:
                conn.execute(
                    text("DELETE FROM subject WHERE \"subject_id\" = :id"),
                    {"id": subject_id}
                )
        except SQLAlchemyError as e:
            print(f"An error occurred during subject deletion: {e}")

    def get_subject(self, subject_id):
        try:
            with self.engine.connect() as conn:
                result = conn.execute(
                    text("SELECT * FROM subject WHERE \"subject_id\" = :id"),
                    {"id": subject_id}
                )
                return result.mappings().first()
        except SQLAlchemyError as e:
            print(f"An error occurred during subject retrieval: {e}")
            return None