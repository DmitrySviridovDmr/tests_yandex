import allure
from ui_yandex.pages.base import Base
from allure_commons.types import AttachmentType


class Checking(Base):
    @allure.step("Проверяем точный текст в элементе")
    def check_text(self, element, expected_text):
        text = self.browser.find_element(*element).text
        if text == expected_text:
            assert True
        else:
            with allure.step("Делаем скриншот бага"):
                allure.attach(
                    self.browser.get_screenshot_as_png(),
                    name="Ожидаемый текст не найден",
                    attachment_type=AttachmentType.PNG)
                assert False
