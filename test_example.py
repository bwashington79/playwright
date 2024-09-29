import re
from playwright.sync_api import Page, expect

msg = "Foo"

def test_has_title(page: Page):
        page.goto("https://playwright.dev/")
        print(msg)
        # Expect a title "to contain" a substring foo.
        expect(page).to_have_title(re.compile("Playwright"))