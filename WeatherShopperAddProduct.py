

import time
from selenium import webdriver
import conf.locators_conf as locators
# from utils.Wrapit import Wrapit
# from page_objects.Base_Page import Base_Page
import re

class weathershopper_tests():

    product_price_element = locators.product_price_element
    product_add_element = locators.product_add_element

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
                  # links = self.driver.find_elements_by_xpath("//button[@class='btn btn-primary' and contains(text(),'Add')]")
                  # click on each of those links
                  # for link in links:
                      # link.location_once_scrolled_into_view
                      # link.click()
                      # time.sleep(5)
                  # print("All items added")         
               else:
                  print("You are on wrong page")               
            else:
               self.driver.find_element_by_xpath("//button[@class='btn btn-primary' and text()='Buy moisturizers']").click()
               is_screen_visible=self.driver.find_element_by_xpath("//h2[contains(text(),'Moisturizers')]")
               if is_screen_visible.is_displayed():
                  print("You are on Buy Moisturizers page")
                  time.sleep(5)
                  #links = self.driver.find_elements_by_xpath("//button[@class='btn btn-primary' and contains(text(),'Add')]")
                  # click on each of those links
                  #for link in links:
                      #link.location_once_scrolled_into_view
                      #link.click()
                      #time.sleep(5)
                  # print("All items added")
               else:
                  print("You are on wrong page")
        
        except Exception as e:
            print(e)
   
    def add_products(self,product_category):
        "Add products to the cart"       
        result_flag = False   
        for product in product_category:
            price_product = 100000          
            product_elements = self.get_elements(self.product_price_element%product)            
            for element in product_elements:                           
                product_price = element.text                                   
                product_price = re.findall(r'\b\d+\b', product_price)                        
                if int(product_price[0]) < price_product:                   
                    price_product = int(product_price[0])                               
            result_flag = self.click_element(self.product_add_element%(product,price_product))
            # self.conditional_write(result_flag,
                                # positive='Successfully added products',
                                # negative='Failed to add products',
                                # level='debug')        
        return result_flag

    def get_elements(self,locator,msg_flag=True):
        "Return a list of DOM elements that match the locator"
        dom_elements = []
        try:
            locator = self.split_locator(locator)
            dom_elements = self.driver.find_elements(*locator)
        except Exception as e:
           
           print(e)
            
        return dom_elements
    
    def click_element(self,locator,wait_time=3):
        "Click the button supplied"
        result_flag = False
        try:            
            link = self.get_element(locator)
            if link is not None:
                link.click()
                result_flag=True
                self.wait(wait_time)
        except Exception as e:
           
           print(e)

        return result_flag
   
    def split_locator(self,locator):
        "Split the locator type and locator"
        result = ()
        try:
            result = tuple(locator.split(',',1))            
        except Exception as e:
            # self.write("Error while parsing locator")
            # self.exceptions.append("Unable to split the locator-'%s' in the conf/locators.conf file"%(locator[0],locator[1]))
           print(e)   
        return result

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    
    weather=weathershopper_tests()
    weather.setUp()
    weather.buy_item()
    weather.tearDown()
    
    
        


    



