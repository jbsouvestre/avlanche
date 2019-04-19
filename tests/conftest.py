import pytest
import yaml


@pytest.fixture(scope='session')
def jekyll_config():
    with open('_config.yml', 'r') as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='session')
def frontlint_config():
    with open('tests/frontlint.yml') as f:
        return yaml.safe_load(f)


@pytest.fixture
def fixture_musique_post():
    return """
        ---
        title: Title
        description: A description
        date: 123
        ---
    """