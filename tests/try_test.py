from pprint import pprint
import pytest


# TODO: see content config
@pytest.mark.skip
def test_view_config(pytestconfig):
    pprint(f"\npytestconfig: {pytestconfig.option}")
    print("*" * 200)
    pprint(f"\ntype pytestconfig: {type(pytestconfig.option)}")
    assert True
