from pages.django_pages.base_page import BasePage
from locators.django_locators.admin_page_locator import AdminPageLocator


class AdminPage(BasePage):

    def admin_is_present(self):
        admin_f = self.find_element(AdminPageLocator.LOCATOR_ADMIN_FORM).text
        assert admin_f == 'Site administration'

    def open_groups(self):
        self.find_element(AdminPageLocator.LOCATOR_GROUPS).click()

    def groups_is_present(self):
        group_f = self.find_element(AdminPageLocator.LOCATOR_GROUPS_TEXT).text
        assert group_f == 'Select group to change'

    def find_group_in_list(self):
        group_list = self.find_elements(AdminPageLocator.LOCATOR_GROUPS_TABLE)
        exist = False
        for i in group_list:
            if 'test' in i.text:
                exist = True
        assert exist is True, "not found"

        print(group_list)
