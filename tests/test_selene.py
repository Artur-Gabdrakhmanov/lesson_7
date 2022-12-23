import allure
import pytest
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s



@pytest.fixture()
def browser_size():
    browser.config.window_width = 1920
    browser.config.window_height = 1080


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'gabdrakhmanov')
@allure.feature('Задачи в репозитории')
@allure.story('"Чистый" тест Selene (без шагов)')
@allure.link('https://github.com', name='Testing')
def test_selene(browser_size):
    browser.open('https://github.com')

    s('.header-search-input').click()
    s('.header-search-input').send_keys('eroshenkoam/allure-example')
    s('.header-search-input').submit()
    s(by.link_text('eroshenkoam/allure-example')).click()
    s("#issues-tab").click()
    s(by.partial_text("#76")).should(be.visible)