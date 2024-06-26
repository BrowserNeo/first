Notes
# 

##  Demoqua_tests
автотест на заполнение и отправку формы https://demoqa.com/automation-practice-form

![2022-08-23_18-21-27](https://user-images.githubusercontent.com/106055633/186198964-c4f7c815-4bd8-43c6-b635-ae1168c652e0.png)



Запушьте код в github-репозиторий и дайте на него ссылку в качестве ответа на домашнее задание.

# Условия:

- Библиотеки, разрешенные к использованию: pytest, selene.

- Можно использовать функции для определения фикстур для прекондишенов к тесту.

- Если часть сценария является прекондишеном к тесту и включает низкоуровневый технический код (например, ожидание догрузки рекламы и удаление ее со страницы с помощью JavaScript)  тогда можно соответствующий код вынести в функцию с читабельным именем, определив ее в этом же файле с тестом.

- Не обязательно, но можно использовать функции для рефакторинга частей кода, которые повторяются, при этом приводя либо к слишком громоздкому коду, либо высокому риску изменений в будущем.

- Нельзя использовать функции с целью создания более читабельных абстракций для действий над элементами.

- Можно использовать переменные для самодокументирования элементов с нечитабельными селекторами. Нечитабельным считается селектор не использующий терминов полностью отображающих пользу элемента на странице. Цель – выжать максимум по "читабельности" из тех селекторов которые можно построить, при этом, стараясь подобрать селекторы максимально стабильные, минимально «хрупкие», минимизируя использование переменных с целью самодокументирования.


#
## Дополнение:

1. Доработать свой код на регистрационную форму с аллюровскими степами


2. Доработать код, чтобы он запускался локально, а браузер в selenoid.autotests.cloud


3. Добавить аттачменты - скриншот, логи консоли, page source, видео


4. Сделать сборку в jenkins.autotests.cloud (регистрация открыта) с кодом


5. Передать из дженкинса адрес удаленного браузера


6. Спрятать логин/пароль к удаленному браузеру в .env файл

___
