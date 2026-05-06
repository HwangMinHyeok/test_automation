from common.action_base import ActionBase
from common.expect_base import ExpectBase
from playwright.sync_api import Page

class Base(ActionBase, ExpectBase):
    def __init__(self, page: Page):
        self.page = page