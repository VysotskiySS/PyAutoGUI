# file: locators.py

class MainLocators:
    base_url_to_img = '../img/'

    SETTINGS_BTN = base_url_to_img+'settings_btn.png'
    CONNECT_BTN = base_url_to_img+'connect_btn.png'
    OK_BTN = base_url_to_img+'ok_btn.png'
    X_BTN = base_url_to_img+'close_connection_window_btn.png'
    FULL_SCREEN_WINDOW_BTN = base_url_to_img+'full_screen_window_btn.png'
    FULL_SCREEN_CS_BTN = base_url_to_img+'full_screen_cs.png'
    UPDATE_TEMP_PASS_BTN = base_url_to_img+'update_temp_pass.png'
    EDIT_TEMP_PASS_BTN = base_url_to_img+'edit_temp_pass.png'
    WARNING_PASS = base_url_to_img+'warning_invalid_email_or_pass.png'
    PASSWORD_WINDOW = base_url_to_img+'need_pass_window.png'


    #2560x1440
    LOGIN_FIELD = (1245, 663)
    PASSWORD_FIELD = (1235, 723)
    LOGIN_BTN = (220, 646)
    LOGOUT_BTN = (220, 672)
    ID_FIELD = (401, 184)

class CSLocators:
    base_url_to_img = '/home/vysotsky/PycharmProjects/PyAutoGUI/img/cs_window/'

    CS_PANEL = base_url_to_img+'cs_panel.png'
    WAIT_IMAGE_POPUP = base_url_to_img + 'wait_image_popup.png'

    # 2560x1440
    X_BTN_FULL_SCREEN_CS = (2540, 17)