# REST API Testing Framework

* [pytest](http://doc.pytest.org/en/latest/)
* [Yandex Allure](http://allure.qatools.ru/)

## Requirements
Python 3.6<br>
Allure 1.4+

## Installation
Execute script:
```bash
sh prepare_env.sh
```

For running all tests, execute:
```bash
py.test
```

## Running tests by Category
You can use pytest fixture for add category to your test, for example:
```python
@pytest.mark.categories(component='logo', suite='smoke', country=['ru','uk'])
```
So test, which has component=log and country=ru, will be found via pytest, other tests will be skipped.
This tests can be running via command
```bash
py.test --categories "component=logo,country=ru"
```

## Reporting
We will be use [Allure reporting](http://allure.qatools.ru/), because it is informative report and it is easy to integrate.
Run pytest with additional parameter alluredir. In this folder allure will be generating XML and other files.
```bash
py.test --alluredir ./var
```
For generating allure report locally, you can use [Allure Commandline](http://wiki.qatools.ru/display/AL/Allure+Commandline)
Generate & open report:
```bash
allure generate ./var
allure open
```