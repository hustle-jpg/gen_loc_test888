from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    TIMEOUT = 10
    wait = WebDriverWait(driver, TIMEOUT)
    URL = 'https://store.steampowered.com'
    driver.get(f'{URL}')

    # Локаторы
    LOGIN_BUTTON_XPATH = "//a[@class='global_action_link']"
    EMAIL_INPUT_XPATH = '//input[@type="text"]'
    PASSWORD_INPUT_XPATH = '//input[@type="password"]'
    SUBMIT_BUTTON_XPATH = "//button[@type='submit']"
    ERROR_MESSAGE_XPATH = "//div[contains(text(), 'Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова.')]"
    error_text = "Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова."

    # Логин
    wait.until(EC.visibility_of_element_located((By.XPATH, LOGIN_BUTTON_XPATH))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, EMAIL_INPUT_XPATH))).send_keys('mail@mail.com')
    wait.until(EC.visibility_of_element_located((By.XPATH, PASSWORD_INPUT_XPATH))).send_keys('password')
    wait.until(EC.element_to_be_clickable((By.XPATH, SUBMIT_BUTTON_XPATH))).click()

    error_message_element = wait.until(EC.visibility_of_element_located((By.XPATH, ERROR_MESSAGE_XPATH)))
    wait.until(EC.text_to_be_present_in_element((By.XPATH, ERROR_MESSAGE_XPATH), error_text))

    # Проверка
    assert error_text == error_message_element.text, f"Expected result: '{error_text}', Actual result: '{error_message_element.text}'"
