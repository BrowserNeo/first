
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



def test_positive(browser_size):
    browser.open('https://google.com/ncr')
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))




def test_negative(browser_size):
    browser.open('https://google.com/ncr')
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selenoid - User-oriented Web UI browser tests in Python'))
