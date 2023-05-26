from seleniumbase import BaseCase


class MyTestClass(BaseCase):

    def test_basics(self):
        self.open("https://www.saucedemo.com/")
