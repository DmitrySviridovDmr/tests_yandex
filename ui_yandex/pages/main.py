from ui_yandex.pages.base import Base
from ui_yandex.pages.locators import *
import allure
import random


main_url = "https://ya.ru/"
email = "testenlil11@yandex.ru"
password = "enlil111"


class Main(Base):
    @allure.step(f"Открываем главную страницу Яндекса {main_url}")
    def open_yandex(self):
        self.open(main_url)

    @allure.step("Авторизуемся под тестовым пользователем")
    def login(self):
        self.wait_for_element(5, MainPageLocators.login_button)
        self.find_element_and_click(MainPageLocators.login_button)
        self.wait_for_element(5, MainPageLocators.email_field)
        self.find_element_and_send(MainPageLocators.email_field, email)
        self.find_element_and_click(MainPageLocators.enter_button)
        self.wait_for_element(5, MainPageLocators.password_field)
        self.find_element_and_send(MainPageLocators.password_field, password)
        self.find_element_and_click(MainPageLocators.enter_button)

    @allure.step("Открываем Яндекс диск")
    def open_ya_disk(self):
        self.wait_for_element(5, MainPageLocators.user_menu)
        self.find_element_and_click(MainPageLocators.user_menu)
        self.find_element_and_click(MainPageLocators.ya_disk_menu)
        self.switch_to(1)
        self.wait_for_element(10, DiskPageLocators.create_button)

    @allure.step("Создаем папку в Яндекс диск")
    def create_folder_ya_disk(self):
        self.find_element_and_click(DiskPageLocators.create_button)
        self.find_element_and_click(DiskPageLocators.create_folder)
        self.clear_input(DiskPageLocators.folder_name_input)
        self.find_element_and_send(
            DiskPageLocators.folder_name_input, f"test{random.randint(1, 999)}"
        )
        self.find_element_and_click(DiskPageLocators.save_folder)
        self.wait_for_element(5, DiskPageLocators.open_saved_folder)
        self.double_click(DiskPageLocators.open_saved_folder)

    @allure.step("Создаем файл в Яндекс диск")
    def create_file_in_folder_ya_disk(self):
        self.find_element_and_click(DiskPageLocators.create_button)
        self.find_element_and_click(DiskPageLocators.create_file)
        self.clear_input(DiskPageLocators.file_name_input)
        self.find_element_and_send(DiskPageLocators.file_name_input, "test_file")
        self.find_element_and_click(DiskPageLocators.save_file)
        self.switch_to(2)
        self.browser.close()
        self.switch_to(1)
        self.wait_for_element(5, DiskPageLocators.file_name)

    @allure.step("Загружаем файл")
    def upload_file_in_folder_ya_disk(self):
        self.find_element_and_send(
            DiskPageLocators.upload_file,
            "C:/Users/sviri/PycharmProjects/tests_yandex"
            "/ui_yandex/file_for_upload.txt",
        )
        self.wait_for_element(5, DiskPageLocators.close_ad_uploaded_file)
        self.find_element_and_click(DiskPageLocators.close_ad_uploaded_file)
        self.double_click(DiskPageLocators.file_name)
        self.switch_to(2)
        self.wait_for_element(10, DiskPageLocators.text_in_uploaded_file)

    @allure.step("Выходим из аккаунта тестового пользователя")
    def logout(self):
        self.open_yandex()
        self.find_element_and_click(MainPageLocators.user_menu)
        self.find_element_and_click(MainPageLocators.exit_menu)
