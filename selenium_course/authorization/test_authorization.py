import json
import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture
def wait(browser):
    return WebDriverWait(browser, 10)

@pytest.fixture(scope="session")
def load_config():
    # Открываем файл с конфигом в режиме чтения
    with open('config.json', 'r') as config_file:
        # С помощью библиотеки json читаем и возвращаем результат
        config = json.load(config_file)
        return config



class TestLogin:
    msgs = ""
    links = ["https://stepik.org/lesson/236895/step/1",
             "https://stepik.org/lesson/236896/step/1",
             "https://stepik.org/lesson/236897/step/1",
             "https://stepik.org/lesson/236898/step/1",
             "https://stepik.org/lesson/236899/step/1",
             "https://stepik.org/lesson/236903/step/1",
             "https://stepik.org/lesson/236904/step/1",
             "https://stepik.org/lesson/236905/step/1"]
    @pytest.mark.parametrize('link', links)
    def test_authorization(self, browser, wait, load_config, link):
        login = load_config['login_stepik']
        password = load_config['password_stepik']
        browser.get(link)
        wait = WebDriverWait(browser, 20)
        login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
        "a.navbar__auth_login")))
        login_button.click()
        browser.find_element(By.ID, "id_login_email").send_keys(login)
        browser.find_element(By.ID, "id_login_password").send_keys(password)
        browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn").click()
        WebDriverWait(browser, 20).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, ".modal-dialog"))
        )
        try:
            start_btn = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.again-btn.white"))
            )
            start_btn.click()
            print('Кнопка "Решить снова" обнаружена, поле textarea неактивное')
            # Если кнопки "Решить снова" не оказалось
        except TimeoutException:
            print('Кнопка "Решить снова" не обнаружена, поле textarea активное')

        finally:
            # Ждем пока поле textarea не очистится и станет активным(пропадет атрибут "disabled"),
            # при этом не используем time.sleep!
            WebDriverWait(browser, 10).until_not(
                EC.element_attribute_to_include((By.CSS_SELECTOR, "textarea.ember-text-area"), 'disabled')
            )
            answer = math.log(int(time.time()))
            input3 = WebDriverWait(browser, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "textarea.ember-text-area"))
            )
            input3.send_keys(answer)
            # Нажимаем кнопку "Отправить"
            button4 = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
            )
            button4.click()
            # Ждем пока не появится фидбек, что ответ верный
            feedback = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "p.smart-hints__hint"))
            )
            #Сравниваем, что фидбек полностью совпадает с "Correct!"
            assert feedback.text == "Correct!", f"{feedback.text}"

