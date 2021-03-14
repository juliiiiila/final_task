from pages.django_pages.main_page import MainPage
from time import sleep


def test_open_admin(browser):
    main_page = MainPage(browser)
    main_page.open_base_page()
    print('ok')
    sleep(5)