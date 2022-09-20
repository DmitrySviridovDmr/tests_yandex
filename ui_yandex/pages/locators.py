from selenium.webdriver.common.by import By

"""Локаторы для главной страницы Яндекса"""


class MainPageLocators:
    login_button = (
        By.XPATH,
        "//a[@class='home-link2 headline__personal-enter home-link2_color_black']",
    )
    email_field = (By.ID, "passp-field-login")
    enter_button = (By.ID, "passp:sign-in")
    password_field = (By.ID, "passp-field-passwd")
    user_menu = (By.XPATH, "//span[@class='avatar__image-wrapper']")
    ya_disk_menu = (By.XPATH, "//span[text()='Диск']")
    exit_menu = (By.XPATH, "//span[text()='Выход']")


"""Локаторы для страницы Яндекс диск"""


class DiskPageLocators:
    create_button = (By.XPATH, "//button[@type='button']")
    upload_file = (By.XPATH, "//input[@type='file']")
    close_ad_uploaded_file = (
        By.XPATH,
        "//button[@class='Button2 Button2_view_clear-inverse Button2_size_m "
        "uploader-progress__close-button']",
    )
    text_in_uploaded_file = (By.XPATH, "//p[@class='mg1']")
    create_folder = (
        By.XPATH,
        "//span[@class='file-icon file-icon_size_m file-icon_dir_plus "
        "create-resource-button__icon']",
    )
    folder_name_input = (By.XPATH, "//input[@text='Новая папка']")
    save_folder = (
        By.XPATH,
        "//button[@class='Button2 Button2_view_action Button2_size_m confirmation-dialog__button "
        "confirmation-dialog__button_submit ']",
    )
    create_file = (
        By.XPATH,
        "//span[@class='file-icon file-icon_size_m file-icon_doc create-resource-button__icon']",
    )
    file_name_input = (By.XPATH, "//input[@text='Новый документ']")
    save_file = (
        By.XPATH,
        "//button[@class='Button2 Button2_view_action Button2_size_m confirmation-dialog__button "
        "confirmation-dialog__button_submit ']",
    )
    open_saved_folder = (
        By.XPATH,
        "//div[@class='listing-item listing-item_theme_tile listing-item_size_m "
        "listing-item_type_dir listing-item_selected js-prevent-deselect']",
    )
    file_name = (By.XPATH, "//span[@class='clamped-text']")
