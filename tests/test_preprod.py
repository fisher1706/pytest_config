import pytest


@pytest.mark.smoke
def test_preprod(env_settings):
    url = env_settings
    print(f"\nurl: {url}")


def test_qa(env_settings):
    url = env_settings
    print(f"\nurl: {url}")
