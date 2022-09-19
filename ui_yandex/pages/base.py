from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys


class Base:
    """Инициализация браузера"""

    def __init__(self, browser):
        self.browser = browser

    """Переходим по ссылке"""

    def open(self, url):
        self.browser.get(url)

    """Находим элемент и кликаем по нему"""

    def find_element_and_click(self, element):
        self.browser.find_element(*element).click()

    """Находим элемент и вводим данные в него"""

    def find_element_and_send(self, element, key):
        self.browser.find_element(*element).send_keys(key)

    """Очищаем поле ввода в элементе"""

    def clear_input(self, element):
        self.browser.find_element(*element).send_keys(Keys.CONTROL + "a")

    """Ждем элемент"""

    def wait_for_element(self, sec, element):
        WebDriverWait(self.browser, sec).until(ec.visibility_of_element_located(element))

    """Переключаемся на вкладку"""

    def switch_to(self, index):
        self.browser.switch_to.window(self.browser.window_handles[index])

    """Двойной клик по элементу"""

    def double_click(self, element):
        ActionChains(self.browser).double_click(self.browser.find_element(*element)).perform()
