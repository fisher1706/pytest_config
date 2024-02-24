import pytest


@pytest.mark.smoke
def test_preprod(env_settings):
    url = env_settings
    print(f"\nurl: {url}")


def test_qa(env_settings):
    url = env_settings
    print(f"\nurl: {url}")


"""
to see pytestconfig
смотрим: "pytestconfig.option.environment"
"""


# @pytest.mark.skip
def test_view_config(pytestconfig):
    # print(f"\npytestconfig: {pytestconfig.option}")
    print(f"\npytestconfig_environment: {pytestconfig.option.environment}")
    print(f"\npytestconfig_markexpr: {pytestconfig.option.markexpr}")
    assert True
