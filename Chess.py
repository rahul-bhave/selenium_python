import unittest, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
 
class SeleniumOnBrowserStack(unittest.TestCase):
    "Example class written to run Selenium tests on BrowserStack"
    def setUp(self):
        self.driver = webdriver.Firefox()
 
    def test_chess(self):
        "An example test: Visit chess.com and click on sign up link"
        #Go to the URL 
        desired_cap = { 'device': 'iPhone 7','realMobile': 'true', 'platform': 'iOS','browserName': 'safari', 'browserstack.debug': 'true' }
        #self.driver = webdriver.Remote(command_executor='http://USERNAME:ACCESS_KEY@hub.browserstack.com:80/wd/hub',desired_capabilities=desired_cap)
        self.driver = webdriver.Remote(command_executor='http://rahulbhave1:rRy4kaY235GNCDAphz9q@hub.browserstack.com:80/wd/hub',desired_capabilities=desired_cap)
        self.driver.get("http://www.chess.com")
        # Assert that the Home Page has title "Chess.com - Play Chess Online - Free Games"
        self.assertIn("Chess.com - Play Chess Online - Free Games", self.driver.title)
        # Identify the xpath for Play Now button which will take you to the sign up page
        elem = self.driver.find_element_by_xpath("//a[@title='Play Now']")
        elem.click()
        time.sleep(5)
        # Print the title of sign up page
        print(self.driver.title)
 
    def tearDown(self):
        self.driver.quit()
 
if __name__ == '__main__':
    unittest.main()