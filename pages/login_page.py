from common.base import Base

class LoginPage(Base):
    # properties
    @property
    def LOGIN_BUTTON(self):
        return self.page.get_by_role("button", name="Login")
    
    @property
    def LOGOUT_BUTTON(self):
        return self.page.get_by_role("link", name="Logout")

    @property
    def EMAIL_INPUT(self):
        return self.page.locator("input[data-qa='login-email']")

    @property
    def PASSWORD_INPUT(self):
        return self.page.locator("input[data-qa='login-password']")
    
    @property
    def INVALID_LOGIN_ERROR(self):
        return self.page.locator("p", has_text="Your email or password is incorrect!")
    
    # actions
    def login(self, email: str, password: str) -> None:
        self.fill(self.EMAIL_INPUT, email)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
    
    # expects
    def expect_login_success(self) -> None:
        self.page.wait_for_url("**/")
        self.expect_visible(self.LOGOUT_BUTTON)
        
        
    def expect_login_failure(self) -> None:
        self.expect_visible(self.INVALID_LOGIN_ERROR)
        