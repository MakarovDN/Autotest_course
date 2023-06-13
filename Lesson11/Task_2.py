# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep


sbis_fix_site = "https://fix-online.sbis.ru/"
contacts_fix_site = "https://fix-online.sbis.ru/page/dialogs"
login = "ЕрохинПро"
password = "ЕрохинПро100"
recipient = "Ерохин Александр"
message = 'Тестовое сообщение'
driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get(sbis_fix_site)
    sleep(2)
    login_input = driver.find_element(By.CSS_SELECTOR, "[name='Login']")
    login_input.send_keys(login)
    further_button = driver.find_elements(By.CSS_SELECTOR, ".auth-AdaptiveLoginForm__loginButtonImage")
    further_button[0].click()
    sleep(1)
    password_input = driver.find_element(By.CSS_SELECTOR, "[name='Password']")
    password_input.send_keys(password)
    further_button[1].click()
    sleep(2)
    driver.get(contacts_fix_site)
    sleep(2)
    new_message = driver.find_element(By.CSS_SELECTOR, ".icon-RoundPlus")
    new_message.click()
    sleep(2)
    search_recipient = driver.find_element(By.CSS_SELECTOR, ".controls-StackTemplate__top-area-content " 
                                                            ".controls-Search__nativeField_caretEmpty")
    search_recipient.send_keys(recipient)
    sleep(2)
    find_recipient = driver.find_element(By.CSS_SELECTOR, ".msg-addressee-item [title='Ерохин Александр']")
    find_recipient.click()
    sleep(2)
    textbox = driver.find_element(By.CSS_SELECTOR, "[role='textbox']")
    textbox.send_keys(message)
    sleep(2)
    send_btn = driver.find_element(By.CSS_SELECTOR, ".icon-BtArrow")
    send_btn.click()
    sleep(2)
    sent_messages = driver.find_elements(By.CSS_SELECTOR, '.msg-dialogs-item p')
    assert sent_messages[0].text == message, 'Отправленное сообщение отсутствует в реестре'
    action_chain = ActionChains(driver)
    action_chain.move_to_element(sent_messages[0])
    action_chain.perform()
    delete_btn = driver.find_element(By.CSS_SELECTOR, ".controls-icon_style-danger")
    delete_btn.click()
    sleep(3)
finally:
    driver.quit()
