import pytest  # Импортируем pytest
from playwright.sync_api import sync_playwright,expect, Page,Playwright  # Имопртируем класс страницы, будем использовать его для аннотации типов
from pytest_playwright.pytest_playwright import context


@pytest.fixture(scope='function')
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    browser.close()