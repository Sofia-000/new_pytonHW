import pytest
from subject import SubjectTable
from sqlalchemy import create_engine

DB = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"


@pytest.fixture(scope="module")
def subject_table():
    engine = create_engine(DB)
    connection = engine.connect()
    transaction = connection.begin()

    subject_table = SubjectTable(DB)

    yield subject_table
    transaction.rollback()
    connection.close()


def test_add(subject_table):
    subject_table.create_subject(11, "Математика")
    subject = subject_table.get_subject(11)
    assert subject is not None
    assert subject["subject_title"] == "Математика"
    subject_table.delete_subject(11)


def test_update(subject_table):
    subject_table.create_subject(12, "История")
    subject_table.update_subject(12, "Всемирная история")
    subject = subject_table.get_subject(12)
    assert subject["subject_title"] == "Всемирная история"
    subject_table.delete_subject(12)


def test_delete(subject_table):
    subject_table.create_subject(13, "Физика")
    subject_table.delete_subject(13)
    subject = subject_table.get_subject(13)
    assert subject is None