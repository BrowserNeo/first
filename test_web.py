from selene.support.shared import browser
from selene import be, have

import pytest


@pytest.fixture()
def before_each():
    print("Alls good")



@pytest.fixture()
def browser_size():
    browser.config.window_width = 1920
    browser.config.window_height = 1080

