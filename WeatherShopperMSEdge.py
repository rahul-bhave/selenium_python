import time
from selenium import webdriver

class weathershopper_tests():

    def setUp(self):
       
       try:     
            edge_path ="C:\\Program Files (x86)\\MicrosoftWebDriver\\MicrosoftWebDriver.exe"
            self.driver = webdriver.Edge(edge_path)
            self.driver.implicitly_wait(10)
            # driver.maximize_window()
            

            self.driver.get("https://weathershopper.pythonanywhere.com")
            # self.driver.maximize_window()
            time.sleep(3)

                 
       except Exception as e:
           
           print(e)
    
if __name__ == "__main__":
    
    weather=weathershopper_tests()
    weather.setUp()
    
        
