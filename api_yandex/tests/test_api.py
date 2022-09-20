import allure
from api_yandex.pages.api import *
from api_yandex.pages.checking import *


class TestYandexDisk:
    @staticmethod
    @allure.title("Тест получения файлов на Яндекс диске")
    @allure.description("Получение файлов на Яндекс диске")
    def test_get_info_about_files():
        result_get: Response = YandexDisk.get_info_about_files()
        Checking.check_status_code(result_get, 200)
        Checking.check_fields_json(result_get, ["items", "limit", "offset"])

    @staticmethod
    @allure.title("Тест получения информации о диске пользователя")
    @allure.description("Получение информации о диске пользователя")
    def test_get_info_about_disk_user():
        result_get: Response = YandexDisk.get_info_about_disk_user()
        Checking.check_status_code(result_get, 200)
        Checking.check_fields_json(
            result_get,
            [
                "max_file_size",
                "paid_max_file_size",
                "total_space",
                "trash_size",
                "is_paid",
                "used_space",
                "system_folders",
                "user",
                "unlimited_autoupload_enabled",
                "revision",
            ],
        )
