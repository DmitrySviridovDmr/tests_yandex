from ui_yandex.pages.main import *
from ui_yandex.pages.checking import *


class TestMain:
    @staticmethod
    @allure.title("Тест создания файла на Яндекс диске")
    @allure.description("Создаем файл на Яндекс диске")
    def test_create_file_in_folder_ya_disk(browser):
        page = Main(browser)
        check = Checking(browser)
        page.open_yandex()
        page.login()
        page.open_ya_disk()
        page.create_folder_ya_disk()
        page.create_file_in_folder_ya_disk()
        check.check_text(DiskPageLocators.file_name, "test_file.docx")
        page.logout()
        check.check_text(MainPageLocators.login_button, "Войти")

    @staticmethod
    @allure.title("Тест загрузки файла на Яндекс диск")
    @allure.description("Загружаем файл на Яндекс диск")
    def test_upload_file_in_folder_ya_disk(browser):
        page = Main(browser)
        check = Checking(browser)
        page.open_yandex()
        page.login()
        page.open_ya_disk()
        page.create_folder_ya_disk()
        page.upload_file_in_folder_ya_disk()
        check.check_text(DiskPageLocators.text_in_uploaded_file, "none")
        page.logout()
        check.check_text(MainPageLocators.login_button, "Войти")
