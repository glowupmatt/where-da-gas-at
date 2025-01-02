from flask_wtf.csrf import generate_csrf
import pytest
from os import getenv

from app import create_app
from app.models import db


def get_test_database_url():
    """get db url from environment, default in-memory sqlite"""
    if getenv("ENV") == "testing-postgres":
        user = getenv("TEST_DB_USER")
        if not user:
            raise Exception("set TEST_DB_USER in environment")
        password = getenv("TEST_DB_PASSWORD")
        if not password:
            raise Exception("set TEST_DB_PASSWORD in environment")
        host = getenv("TEST_DB_HOST")
        if not host:
            raise Exception("set TEST_DB_HOST in environment")
        port = getenv("TEST_DB_PORT")
        if not port:
            raise Exception("set TEST_DB_PORT in environment")
        database = getenv("TEST_DB_NAME")
        if not database:
            raise Exception("set TEST_DB_NAME in environment")
        schema = getenv("TEST_DB_SCHEMA")
        if not schema:
            raise Exception("set TEST_DB_SCHEMA in environment")

        return (
            "postgres://"
            + user
            + ":"
            + password
            + "@"
            + host
            + ":"
            + port
            + "/"
            + database
            + "?options=-c search_path="
            + schema
        )
    return "sqlite:///:memory:"


@pytest.fixture(scope="session")
def app():
    _app = create_app(
        {
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": get_test_database_url(),
            "SQLALCHEMY_TRACK_MODIFICATIONS": False,
            "WTF_CSRF_ENABLED": True,
        }
    )

    with _app.app_context():
        db.create_all()

        yield _app

        db.session.remove()
        db.drop_all()


@pytest.fixture(scope="function")
def db_session(app):
    """create a fresh db session for a test, clear tables after"""
    with app.app_context():
        connection = db.engine.connect()
        transaction = connection.begin()

        session = db.create_scoped_session(
            options={"bind": connection, "binds": {}}
        )

        db.session = session

        yield session

        transaction.rollback()
        connection.close()
        session.remove()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def test_king(app):
    from app.models import King, db

    king = King(
        nick="kingifer",
        email="king@example.com",
        password="password",
    )

    db.session.add(king)
    db.session.commit()

    yield king

    db.session.delete(king)
    db.session.commit()
