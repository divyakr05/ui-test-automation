from playwright.sync_api import expect
from pages.home_page import HomePage
from tests.base_test import BaseTest


class TestHome(BaseTest):

    def test_verify_package_details(self, set_up):
        """
        Verify package details.
        """
        country = "Japan"
        exp_title = "Moshi Moshi"
        exp_coverage_value = "Japan"
        exp_data_value = "1 GB"
        exp_validity_value = "7 Days"
        exp_price_value = "$4.50"
        page = set_up
        self.home_page = HomePage(page)
        self.home_page.accept_cookie_popup()
        self.home_page.cancel_push_notifications()
        self.home_page.search_destination(country)
        self.home_page.select_local_destination_from_auto_complete()
        self.home_page.click_buy_now_button()
        expect(self.home_page.get_package_title_locator()).to_have_text(exp_title)
        expect(self.home_page.get_coverage_value_locator()).to_have_text(exp_coverage_value)
        expect(self.home_page.get_data_value_locator()).to_have_text(exp_data_value)
        expect(self.home_page.get_validity_value_locator()).to_have_text(exp_validity_value)
        expect(self.home_page.get_price_value_locator()).to_have_text(exp_price_value)

