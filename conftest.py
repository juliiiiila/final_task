import pytest
from selenium import webdriver
from settings import DB_URL
from framework.db.postgres.db_steps import DBSteps


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()


db_steps = DBSteps(DB_URL)
print(db_steps.get_user_in_group())
