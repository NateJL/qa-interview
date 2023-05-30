from seleniumbase import BaseCase
from selenium.webdriver.common.by import By
import pytest
from parameterized import parameterized

#
# From what I gathered online, inheriting from the "BaseCase" class prohibits the use of
# Pytest "parametrization" (ie. running the same test using different parameters).  I was able to find another library (parameterized) 
# that was able to handle that functionality for me.
#
class MyTestClass(BaseCase):

    #
    # Simple base test case so test if the web page loads as expected
    #
    @pytest.mark.active
    def test_basics(self):
        self.open("https://www.saucedemo.com/")
        self.assert_title("Swag Labs")


    #
    # Test case to check for valid login using valid credentials
    #
    @pytest.mark.active
    def test_login_valid_credentials(self):
        self.open("https://www.saucedemo.com/")
        self.type("input#user-name", "standard_user")
        self.type("input#password", "secret_sauce")
        self.click("input#login-button")

        assert(self.get_current_url() == "https://www.saucedemo.com/inventory.html")


    #
    # Test case to check for invalid login using invalid credentials
    #
    @pytest.mark.active
    def test_login_invalid_credentials(self):
        self.open("https://www.saucedemo.com/")
        self.type("input#user-name", "nonstandard_user")
        self.type("input#password", "secret_sauce")
        self.click("input#login-button")

        self.assert_element("div.error-message-container")
    

    #
    # Test case to check for login attempts for a locked out user account
    #
    @pytest.mark.active
    def test_login_lockout_credentials(self):
        self.open("https://www.saucedemo.com/")
        self.type("input#user-name", "locked_out_user")
        self.type("input#password", "secret_sauce")
        self.click("input#login-button")

        self.assert_element("button.error-button")

    #
    # Test case to check for problem user account
    #
    @pytest.mark.active
    def test_login_problem_user(self):
        self.open("https://www.saucedemo.com/")
        self.type("input#user-name", "problem_user")
        self.type("input#password", "secret_sauce")
        self.click("input#login-button")

        # To properly build out the test case the way I would like would take longer than is desired for this assignment, but
        # would essentially be as follows after looking at the issues that plagued the account:
        # 1.) Login
        # 2.) For each item in the inventory list
        #       2.1) Verify the item image is correct
        #       2.2) Verify the item link brings the user to the correct item page
        #
        # This could be implemented in the "test_inventory_element" test case if logged in with a user that has this issue


    #
    # Test case to check the shop landing page (after user has logged in) for expected elements
    # Pretty barebones in terms of testing, but additional checks can be easily added as needs arise.
    #
    @pytest.mark.active
    def test_landing_page_content(self):
        self.open("https://www.saucedemo.com/")
        self.type("input#user-name", "standard_user")
        self.type("input#password", "secret_sauce")
        self.click("input#login-button")
        
        self.assert_element("div.inventory_list")
        self.assert_element("div.bm-burger-button")
        self.assert_element("a.shopping_cart_link")


    #
    # Test case to check items in the shop for a valid, logged in, standard user.
    # From what I read online, Selenium and the built-in "parametrize" functionality for PyTest don't always play nice together,
    # therefore I used the "parameterized" library to make the implementation more straightforward.
    #
    # I originally was going to programatically collect the items in the shop then test for them individually, but with respect for time I
    # decided it would be more efficient to simply hardcode the desired test items.
    #
    @parameterized.expand([
        ("sauce-labs-backpack", "4"),
        ("sauce-labs-bike-light", "0"),
        ("sauce-labs-bolt-t-shirt", "1"),
        ("sauce-labs-fleece-jacket", "5"),
        ("sauce-labs-onesie", "2"),
    ])
    @pytest.mark.active
    def test_inventory_element(self, item_name, item_num):
        print("\n" + item_name + "\n")
        self.open("https://www.saucedemo.com/")
        self.type("input#user-name", "standard_user")
        self.type("input#password", "secret_sauce")
        self.click("input#login-button")

        # Select the "Add to cart" button and verify changes
        self.click("button#add-to-cart-" + item_name)
        self.assert_element("button#remove-" + item_name)
        self.assert_element("span.shopping_cart_badge")

        # Select "Remove from cart" button and verify changes
        self.click("button#remove-" + item_name)
        self.assert_element("button#add-to-cart-" + item_name)

        # Select item title and verify window change
        self.click("a#item_" + item_num + "_title_link")
        assert(self.get_current_url() == "https://www.saucedemo.com/inventory-item.html?id=" + item_num)
        self.assert_element("button#add-to-cart-" + item_name)
        self.click("button#add-to-cart-" + item_name)
        self.assert_element("button#remove-" + item_name)
        self.click("button#remove-" + item_name)





