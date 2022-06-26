from selene import have, command
from selene.support.shared import browser


def test_form():
    browser.open('/')


    browser.element('#firstName').type('Avraam')
    browser.element('#lastName').type('Neo')
    browser.element('#userEmail').type('figaro@gmail.com')
    browser.element('#userNumber').type('1234567890')
    browser.element('#currentAddress').type('Neverland')

    browser.element('[class="custom-control-label"]').should(have.exact_text('Male')).click()

    browser.element('[class="custom-control-label"][for="hobbies-checkbox-3"]').should(have.exact_text('Music')).click()

    browser.element('')



    browser.element('#submitCLEAN').click()





