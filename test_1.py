from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker


fake = Faker()

LOGIN_BUTTON = (By.XPATH, "//a[@class='global_action_link']")
EMAIL_INPUT = (By.XPATH, '//input[@type="text"]')
PASSWORD_INPUT = (By.XPATH, '//input[@type="password"]')
SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
ERROR_MESSAGE = (By.XPATH, "//div[contains(text(), 'Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова.')]")
EXPECTED_ERROR_TEXT = "Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова."
TIMEOUT = 10
URL = 'https://store.steampowered.com'

def test_login(driver):
    wait = WebDriverWait(driver, TIMEOUT)
    driver.get(f'{URL}')

    email = fake.email()
    password = fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)

    wait.until(EC.element_to_be_clickable(LOGIN_BUTTON)).click()
    wait.until(EC.visibility_of_element_located(EMAIL_INPUT)).send_keys(email)
    wait.until(EC.visibility_of_element_located(PASSWORD_INPUT)).send_keys(password)
    wait.until(EC.element_to_be_clickable(SUBMIT_BUTTON)).click()

    actual_error_text = wait.until(EC.visibility_of_element_located(ERROR_MESSAGE)).text
    assert actual_error_text == EXPECTED_ERROR_TEXT, f"Expected result: '{EXPECTED_ERROR_TEXT}', Actual result: '{actual_error_text}'"
