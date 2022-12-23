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
@allure.story('Тест с применением Лямбда шагов через with allure.step')
@allure.link('https://github.com', name='Testing')
def test_dynamic_steps(browser_size):
    with allure.step('Открываем главную страницу'):
        browser.open('https://github.com')

    with allure.step('Ищем репозитории'):
        s('.header-search-input').click()
        s('.header-search-input').send_keys('eroshenkoam/allure-example')
        s('.header-search-input').submit()

    with allure.step('переходим по ссылке репозитория'):
        s(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Открываем таб Issues'):
        s("#issues-tab").click()

    with allure.step('Проверяем наличие Issue с номером 76'):
        s(by.partial_text("#76")).should(be.visible)


@allure.tag('web')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'gabdrakhmanovar')
@allure.feature('Задачи в репозитории')
@allure.story('Тест с применением шагов с декоратором @allure.step')
@allure.link('https://github.com', name='Testing')
def test_decorator_steps(browser_size):
    open_main_page()
    search_for_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    open_issue_tab()
    should_see_ussue_with_number('#76')


@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open('https://github.com')

@allure.step('Ищем репозитории {repo}')
def search_for_repository(repo):
    s('.header-search-input').click()
    s('.header-search-input').send_keys(repo)
    s('.header-search-input').submit()

@allure.step('переходим по ссылке репозитория {repo}')
def go_to_repository(repo):
    s(by.link_text(repo)).click()

@allure.step('Открываем таб Issues')
def open_issue_tab():
    s("#issues-tab").click()


@allure.step('Проверяем наличие Issue с номером {number}')
def should_see_ussue_with_number(number):
    s(by.partial_text(number)).click()