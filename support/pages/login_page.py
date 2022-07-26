"""
Login page.
"""
from playwright.sync_api import Page
from support.modules.web_driver import WebDriver


class LoginPage(WebDriver):
    """
    Login Page class.
    """

    """path static"""
    path = "?controller=authentication&back=my-account"

    """locators"""
    _input_login = "#email"
    _input_password = "#passwd"
    _input_email = "#email_create"
    _btn_login = "#SubmitLogin"
    _btn_create_account = "#SubmitCreate"
    _link_forgot_password = ""
    _panel_alert_create = "#create_account_error"
    _panel_alert = ".alert-danger"
    _panel_alert_reasons = "//*[@class='alert alert-danger']//li"

    """methods"""

    def __init__(self, page: Page):
        super().__init__(page, self.path)

    def enter_login(self, login):
        """
        Insert login to login field.
        :param login:
        """
        self.fill_field(login, self._input_login)

    def enter_password(self, password):
        """
        Insert password to password field.
        :param password:
        """
        self.fill_field(password, self._input_password)

    def enter_email(self, email):
        """
        Insert email to email field to create account.
        :param email:
        :return:
        """
        self.fill_field(email, self._input_email)

    def click_login_button(self):
        """
        Click on login button.
        """
        self.click(self._btn_login)

    def click_create_account(self):
        """
        Click on create account button.
        """
        self.click(self._btn_create_account)

    def click_forgot_password(self):
        """
        Click link "Forgot password?"
        """
        self.click(self._link_forgot_password)
        # return PasswordPage

    def login(self, login: str = "", password: str = ""):
        """
        Log in to platform inserting login and password.
        :param login:
        :param password:
        """
        self.enter_login(login)
        self.enter_password(password)
        self.click_login_button()
