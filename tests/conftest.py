# conftest.py
import pytest
from blogexample.app import create_app, db
from config.settings import TestingConfig

@pytest.fixture(scope='module')
def app():
    """Create and configure a new app instance for each test module."""
    _app = create_app(TestingConfig)
    with _app.app_context():
        db.create_all()
        yield _app
        db.session.remove()
        db.drop_all()

@pytest.fixture(scope='module')
def test_client(app):
    """A test client using the Flask app configured for tests."""
    return app.test_client()

@pytest.fixture(scope='function')
def session(app):
    """Create a new database session for each test function, with changes rolled back afterwards."""
    try:
        with app.app_context():
            # Flask-SQLAlchemy tracks transactions per app context, so just start a transaction
            transaction = db.session.begin_nested()

            yield db.session

            # Roll back transaction and remove session
            transaction.rollback()
            db.session.remove()
    except:
        pass