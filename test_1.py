from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    driver.get('https://store.steampowered.com')

    # Локаторы
    login_button_xpath = "//a[@class='global_action_link']"
    email_input_xpath = '//input[@class="_2GBWeup5cttgbTw8FM3tfx" and @type="text"]'
    password_input_xpath = '//input[@class="_2GBWeup5cttgbTw8FM3tfx" and @type="password"]'
    submit_button_xpath = "//button[@class='DjSvCZoKKfoNSmarsEcTS']"
    error_message_xpath = "//div[@class='_1W_6HXiG4JJ0By1qN_0fGZ']"
    error_text = "Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова."

    # Логин
    wait.until(EC.element_to_be_clickable((By.XPATH, login_button_xpath))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, email_input_xpath))).send_keys('mail@mail.com')
    wait.until(EC.element_to_be_clickable((By.XPATH, password_input_xpath))).send_keys('password')
    wait.until(EC.element_to_be_clickable((By.XPATH, submit_button_xpath))).click()

    error_message_element = wait.until(EC.visibility_of_element_located((By.XPATH, error_message_xpath)))
    wait.until(EC.text_to_be_present_in_element((By.XPATH, error_message_xpath), error_text))

    # Проверка
    assert error_text == error_message_element.text
