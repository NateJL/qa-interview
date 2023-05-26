# seleniumbase-qa-interview
This is based off and using www.seleniumbase.io

# Pre-requisites
Having the following installed
* python
* pip
* seleniumbase.io

Selenium base has good documentation how to install python, pip and sbase here (This will also take care of all webdriver needs)
https://seleniumbase.io/help_docs/install_python_pip_git/

From there you can install seleniumbase with pip: ```pip install seleniumbase```

# Fork this project and create a pull request on your own repo and send me the link.
# Don't spend too much time on this assignment, it's expected to be done within 2 hours.

# Write test cases for MyTestClass(BaseCase):
```
class MyTestClass(BaseCase):

    def test_basics(self):
        self.open("https://www.saucedemo.com/")
        
    # after landing on the login page, use the credentials provided on the screen to login.
    # Explore and create a suite of selenium test cases to test the functionality of this application.

 ```

# How to run the test file
```
pytest qa_interview_test.py      
```

# Submit
After completing the task, zip your test files and email it back.

# Useful documentation link
https://github.com/seleniumbase/SeleniumBase/blob/master/seleniumbase/fixtures/base_case.py
