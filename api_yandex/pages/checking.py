from requests import Response
import json


class Checking:
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        print(f"Статус код верен: {status_code}")

    @staticmethod
    def check_fields_json(response: Response, expected_value):
        fields = json.loads(response.text)
        assert list(fields) == expected_value
        print("Все поля верны")
