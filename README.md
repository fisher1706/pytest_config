# -----------------------------------PYTEST.CONFIG----------------------------------------------------------------------
# dir -> "pytest_config_separate_tests"

# PYTEST.CONFIG -> хранятся все настройки pytest

# идея -> добавляем один аргумент(необязательный) -> формируются разные данные для тестов -> разделяем тесты на два 
# env -> --environment=preprod

# conftest.py -> содержит: fixtures, hooks, plugins

# start tests preprod
```shell
pytest -s -v --environment='preprod' tests/
```

# start tests qa
```shell
pytest -s -v tests/
```