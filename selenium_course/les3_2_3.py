from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
import time
import unittest

class TestLink(unittest.TestCase):

    def test_link1(self):
        fake = Faker()
        email = fake.email()
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.TAG_NAME, "input")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block div.form-group.second_class input")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CLASS_NAME, "third")
        input3.send_keys(email)

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Текст не совпадает с ожидаемым")

    def test_link2(self):
        fake = Faker()
        email = fake.email()
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.TAG_NAME, "input")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block div.form-group.second_class input")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CLASS_NAME, "third")
        input3.send_keys(email)

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Текст не совпадает с ожидаемым")

    if __name__ == "__main__":
        unittest.main()