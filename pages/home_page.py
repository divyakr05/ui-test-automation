from pages.base_page import BasePage
from playwright.sync_api import Page


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.current_page = page
        self.ACCEPT_BUTTON = page.locator("//button[text()='ACCEPT']")
        self.CANCEL_PUSH_NOTIFICATION = page.locator("//button[@id='wzrk-cancel']")
        self.SEARCH_FIELD = page.locator("//div[@class='inp-search-container']/input")
        self.AUTO_COMPLETE_POPUP = page.locator(
            "//div[contains(@class,'homepage_country')]/ul[contains(@class,'countries-list position-absolute')]")
        self.AUTO_COMPLETE_LOCAL = page.locator("//div[contains(@class,'homepage_country')]/ul//p[text()='Local']")
        self.AUTO_COMPLETE_LOCAL_DEST = page.locator("(//ul//span[@class='country-name'])[1]")
        self.BUY_NOW_BUTTON = page.locator("(//button[@type='button'][normalize-space()='BUY NOW'])[1]")
        self.PACKAGE_TITLE = page.locator("//div[@class='sim-detail-operator']//p")
        self.DETAIL_INFO_COVERAGE = page.locator("//ul[contains(@class,'sim-detail-info-list')]//p[text()='COVERAGE']")
        self.COVERAGE_VALUE = page.locator(
            "//ul[@data-testid='sim-detail-info-list']//p[@data-testid='COVERAGE-value']")
        self.DETAIL_INFO_DATA = page.locator(
            "//ul[@class='sim-detail-info-list']//p[@class='key sim-item-row-left-key'][normalize-space()='DATA']")
        self.DATA_VALUE = page.locator("//ul[@data-testid='sim-detail-info-list']//p[@data-testid='DATA-value']")
        self.DETAIL_INFO_VALIDITY = page.locator(
            "//ul[@class='sim-detail-info-list']//p[@class='key sim-item-row-left-key'][normalize-space()='VALIDITY']")
        self.VALIDITY_VALUE = page.locator(
            "//ul[@data-testid='sim-detail-info-list']//p[@data-testid='VALIDITY-value']")
        self.DETAIL_INFO_PRICE = page.locator(
            "//ul[@class='sim-detail-info-list']//p[@class='key sim-item-row-left-key'][normalize-space()='PRICE']")
        self.PRICE_VALUE = page.locator("//ul[@data-testid='sim-detail-info-list']//p[@data-testid='PRICE-value']")

    # Accept the cookie popup
    def accept_cookie_popup(self):
        self.ACCEPT_BUTTON.click()

    # Cancel the push notifications popup
    def cancel_push_notifications(self):
        self.CANCEL_PUSH_NOTIFICATION.click()

    # Search for a region/country in the search field
    def search_destination(self, destination):
        self.SEARCH_FIELD.fill(destination)

    # Select the destination from the “Local” section in the autocomplete options
    def select_local_destination_from_auto_complete(self):
        self.AUTO_COMPLETE_POPUP.wait_for(timeout=3_000)
        if self.AUTO_COMPLETE_POPUP.is_visible():
            self.AUTO_COMPLETE_LOCAL_DEST.click()

    # Click on "Buy Now" button of the first package
    def click_buy_now_button(self):
        self.BUY_NOW_BUTTON.click()

    # Get locator of the package title
    def get_package_title_locator(self):
        return self.PACKAGE_TITLE

    # Get locator of the COVERAGE value
    def get_coverage_value_locator(self):
        return self.COVERAGE_VALUE

    # Get locator of the DATA value
    def get_data_value_locator(self):
        return self.DATA_VALUE

    # Get locator of the VALIDITY value
    def get_validity_value_locator(self):
        return self.VALIDITY_VALUE

    # Get locator of the PRICE value
    def get_price_value_locator(self):
        return self.PRICE_VALUE
