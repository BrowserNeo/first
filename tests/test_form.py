from selene import have
from selene.support.shared import browser

firstname = 'Avraam'
lastname = 'Neo'
email = 'figaro@gmail.com'
gender = 'Male'
usernumber = '1234567890'
hobbies = 'Music'
currentaddress = 'Neverland'
data = '22 Jun 1990'


def test_form():
    browser.open('/')


    browser.element('#firstName').type(firstname)
    browser.element('#lastName').type(lastname)
    browser.element('#userEmail').type(email)
    browser.element('#userNumber').type(usernumber)
    browser.element('#currentAddress').type(currentaddress)

    browser.element('[class="custom-control-label"]').should(have.exact_text(gender)).click()

    browser.element('[class="custom-control-label"][for="hobbies-checkbox-3"]').should(have.exact_text(hobbies)).click()

    browser.element('#dateOfBirthInput').click()
    browser.element('#dateOfBirthInput').type(data)






    browser.element('#submitCLEAN').click()





