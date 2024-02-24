import pytest


"""
1. добавляем хуком "pytest_addoption" переменную "environment" в "pytestconfig"
"""


def pytest_addoption(parser):
    parser.addoption(
        "--environment",
        action="store",
        default="qa",
        help="target environment"
    )


"""
2. формируем url в зависимости от переменной "environment"
"""


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


"""
3. формируем хуком "pytest_configure" скоп тестов в зависимости от значения "environment" -> тесты для "preprod"
"""


def pytest_configure(config):
    if config.option.environment == 'preprod':
        config.option.markexpr = 'smoke'
    else:
        config.option.markexpr = 'not smoke'
