

import time
from selenium import webdriver
import conf.locators_conf as locators
# from utils.Wrapit import Wrapit
# from page_objects.Base_Page import Base_Page
import re

class weathershopper_tests():

    def setUp(self):
       
       try:     
            self.driver=webdriver.Chrome()
            self.driver.get('https://weathershopper.pythonanywhere.com')
            self.driver.maximize_window()
            if(self.driver.title=="The best moisturizers in the world!"):
               print ("Success: The best moisturizers in the world!")
            else:
               print ("Failed: Title is incorrect") 
                 
       except Exception as e:
           
           print(e)

    def buy_item(self):

        try:
            temp=self.driver.find_element_by_xpath("//span[@id='temperature']")
            print("The temperature is %s"%temp.text)
            print("The temperature in bytes is %s"%temp.text.encode('utf-8'))
            
            if (temp.text.encode('utf8'))>= bytes('20','utf-8'):
               self.driver.find_element_by_xpath("//button[@class='btn btn-primary' and text()='Buy sunscreens']").click()
               is_screen_visible=self.driver.find_element_by_xpath("//h2[contains(text(),'Sunscreens')]")
               if is_screen_visible.is_displayed():
                  print("You are on Buy Sunscreens page")
                  time.sleep(5)

                  links = self.driver.find_elements_by_xpath("//button[@class='btn btn-primary' and contains(text(),'Add')]")
                  # click on each of those links
                  for link in links:
                      link.location_once_scrolled_into_view
                      link.click()
                      time.sleep(5)
                  print("All items added")

               else:
                  print("You are on wrong page")
                
            else:
               self.driver.find_element_by_xpath("//button[@class='btn btn-primary' and text()='Buy moisturizers']").click()
               is_screen_visible=self.driver.find_element_by_xpath("//h2[contains(text(),'Moisturizers')]")
               if is_screen_visible.is_displayed():
                  print("You are on Buy Moisturizers page")
                  time.sleep(5)
                  links = self.driver.find_elements_by_xpath("//button[@class='btn btn-primary' and contains(text(),'Add')]")
                  # click on each of those links
                  for link in links:
                      link.location_once_scrolled_into_view
                      link.click()
                      time.sleep(5)
                  print("All items added")

               else:
                  print("You are on wrong page")
        


        except Exception as e:
            print(e)


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    
    weather=weathershopper_tests()
    weather.setUp()
    weather.buy_item()
    weather.tearDown()
    
    
        


    



