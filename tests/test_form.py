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
month = 'April'
state = 'NCR'


def test_form():
    browser.open('/')


    browser.element('#firstName').type(firstname)
    browser.element('#lastName').type(lastname)
    browser.element('#userEmail').type(email)
    browser.element('#userNumber').type(usernumber)
    browser.element('#currentAddress').type(currentaddress)

    browser.element('[class~="custom-control-label"]').should(have.exact_text(gender)).click()

    browser.element('[class~="custom-control-label"][for="hobbies-checkbox-3"]').should(have.exact_text(hobbies)).click()

    browser.element('#dateOfBirthInput').click()

    browser.element('[class~="react-datepicker__month-select"]').element('[value="8"]').click()

    browser.element('[class~="react-datepicker__year-select"]').element('[value="1994"]').click()

    browser.element('[class~="react-datepicker__day--015"]').click()

    # Дата рождения - сделал костыльно, т.к. не понял как работает clear() в этой графе

    browser.element('#subjectsContainer').click().should(have.exact_text("History")).click()

    # Не сделал!!! Current address Вообщем я пока здесь остановился но уже начинается разбор ДЗ. Пойду смотреть.

    browser.element('#state').click().should(have.exact_text(state)).click()












    browser.element('#submitCLEAN').click()





