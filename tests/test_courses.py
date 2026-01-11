import pytest
from playwright.sync_api import sync_playwright, expect

from tests.conftest import chromium_page_with_state


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
        # Нажимаем на кнопку Login

        # Проверяем, что появилось сообщение об ошибке
        # wrong_email_or_password_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')
        # expect(wrong_email_or_password_alert).to_be_visible()
        # expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")

    courses = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses).to_have_text('Courses')
    expect(courses).to_be_visible()

    icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(icon).to_be_visible()

    result_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(result_text).to_have_text('There is no results')
    expect(result_text).to_be_visible()

    paragraph_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(paragraph_text).to_have_text('Results from the load test pipeline will be displayed here')
    expect(paragraph_text).to_be_visible()
