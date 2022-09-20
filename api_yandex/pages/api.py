from api_yandex.pages.http_method import HttpMethod

base_url = 'https://cloud-api.yandex.net/v1/disk'


class YandexDisk:
    @staticmethod
    def get_info_about_files():
        get_resource = "/resources/files"
        get_url = base_url + get_resource
        print(f"\n{get_url}")
        result_get = HttpMethod.get(get_url)
        print(result_get.text)
        return result_get

    @staticmethod
    def get_info_about_disk_user():
        print(f"\n{base_url}")
        result_get = HttpMethod.get(base_url)
        print(result_get.text)
        return result_get
