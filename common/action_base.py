from playwright.sync_api import Locator

class ActionBase:
    def click(self, target: str | Locator, **kwargs) -> None:
        if isinstance(target, Locator):
            target.click()
        else:
            self.page.locator(target, **kwargs).click()

    def fill(self, target: str | Locator, value: str, **kwargs) -> None:
        if isinstance(target, Locator):
            target.fill(value)
        else:
            self.page.locator(target, **kwargs).fill(value)