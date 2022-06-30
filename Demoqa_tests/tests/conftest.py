from selene.support.shared import browser
import pytest


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.config.hold_browser_open = True
    browser.config.window_height = '1080'
    browser.config.window_width = '1600'