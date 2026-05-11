from playwright.sync_api import Locator, expect
        
class ExpectBase:
    def expect_visible(self, target: str | Locator, **kwargs) -> None:
        if isinstance(target, Locator):
            expect(target).to_be_visible()
        else:
            expect(self.page.locator(target, **kwargs)).to_be_visible()
            
    def expect_not_visible(self, target: str | Locator, **kwargs) -> None:
        if isinstance(target, Locator):
            expect(target).not_to_be_visible()
        else:
            expect(self.page.locator(target, **kwargs)).not_to_be_visible()
            
    def expect_enabled(self, target: str | Locator, **kwargs) -> None:
        if isinstance(target, Locator):
            expect(target).to_be_enabled()
        else:
            expect(self.page.locator(target, **kwargs)).to_be_enabled()