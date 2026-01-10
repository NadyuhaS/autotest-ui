from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Переходим на страницу входа
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Заполняем поле email
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill("user.name@gmail.com")

    email_input = page.get_by_test_id('registration-form-username-input').locator('input')
    email_input.fill("username")

    # Заполняем поле пароль
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill("password")

    reg_button = page.get_by_test_id('registration-page-registration-button')
    reg_button.click()

    context.storage_state(path="browser-state.json")

    context_new = browser.new_context(storage_state="browser-state.json")
    page = context_new.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    # Нажимаем на кнопку Login


    # Проверяем, что появилось сообщение об ошибке
    # wrong_email_or_password_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')
    # expect(wrong_email_or_password_alert).to_be_visible()
    # expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")

    courses = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses).to_have_text('Courses')
    expect(courses).to_be_visible()

    icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(icon).to_be_visible()

    result_text = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(result_text).to_have_text('There is no results')
    expect(result_text).to_be_visible()

    paragraph_text = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(paragraph_text).to_have_text('Results from the load test pipeline will be displayed here')
    expect(paragraph_text).to_be_visible()



    # Задержка для наглядности выполнения теста (не рекомендуется использовать в реальных автотестах)
    page.wait_for_timeout(5000)

