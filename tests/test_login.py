import pytest
import allure
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@allure.story('Login Feature')
@allure.title('Авторизаиция с недействительными учетными данными')
def test_login_failure(login_page):
    with allure.step('Открыть страницу авторизации'):
        login_page.navigate()
    with allure.step('Ввести в форму авторизации недействительные учетные данные'):
        login_page.login("invalid_user", "invalid_password")
    with allure.step('Url не изменился'):
        login_page.check_url("https://zimaev.github.io/pom/")
    with allure.step('Отображается ошибка - Invalid credentials. Please try again.'):
        assert login_page.get_error_message() == 'Invalid credentials. Please try again.'


@allure.story('Login Feature')
@allure.title('Авторизаиция с корректными учетными данными')
@pytest.mark.parametrize('username, password', [
    ('user', 'user'),
    ('admin', 'admin')
])
def test_login_success(login_page, dashboard_page, username, password):
    with allure.step('Открыть страницу авторизации'):
        login_page.navigate()
    with allure.step('Ввести в форму авторизации действительные учетные данные'):
        login_page.login(username, password)
    with allure.step('Отображается приветственное сообщение с именем пользователя'):
        dashboard_page.assert_welcome_message(f"Welcome {username}")
