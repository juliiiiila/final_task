from selenium.webdriver.common.by import By


class AdminPageLocator:

    LOCATOR_ADMIN_FORM = (By.XPATH, '//div[@id="content"]/h1')
    LOCATOR_GROUPS = (By.XPATH, '//a[@href="/admin/auth/group/"]')
    LOCATOR_GROUPS_TEXT = (By.XPATH, '//div[@id="content"]/h1')
    LOCATOR_GROUPS_TABLE = (By.CLASS_NAME, 'field-__str__')
