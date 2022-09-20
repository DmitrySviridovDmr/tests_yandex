import allure
import requests


class HttpMethod:
    token = "y0_AgAAAABksblRAADLWwAAAADPSP_CxkDD6a4sTceWbcoxZwRxgfXdmn4"
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}

    @staticmethod
    def get(url):
        with allure.step("Метод GET"):
            result = requests.get(url, headers=HttpMethod.headers)
            return result
