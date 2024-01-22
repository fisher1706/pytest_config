import pytest


# TODO: pytest --environment='preprod' -vs -> start tests on "preprod"
def pytest_addoption(parser):
    parser.addoption(
        "--environment",
        action="store",
        default="qa",
        help="target environment"
    )


def pytest_configure(config):
    if config.option.environment == 'preprod':
        config.option.markexpr = 'smoke'
    else:
        config.option.markexpr = 'not smoke'


@pytest.fixture(scope="session")
def env_settings(pytestconfig):
    url_set = get_urls(pytestconfig.getoption('--environment'))
    return url_set


def get_urls(env):
    if env == 'preprod':
        url = 'https://preprod.lamoda.ru'
    else:
        url = 'https://qa.lamoda.ru'
    return url
