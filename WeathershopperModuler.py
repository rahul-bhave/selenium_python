

import time
from selenium import webdriver

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
                  
                  
                  # self.driver.find_element_by_xpath("//button[@class='btn btn-primary' and contains(@onclick,'Robert Herbals Sunblock SPF-40')]").click()
                  # time.sleep(5)
                  # self.driver.find_element_by_xpath("//button[@class='btn btn-primary' and contains(@onclick,'Paul Magnificient SPF-30')]").click()
                  # time.sleep(5)
                  # self.driver.find_element_by_xpath("//button[@class='btn btn-primary' and contains(@onclick,'Vishy La Shield Sunscreen spf-30')]").click()
                  # time.sleep(5)
                  # self.driver.find_element_by_xpath("//button[@class='btn btn-primary' and contains(@onclick,'Vassily Brilliant SPF-30')]").click()
                  # time.sleep(5)
                  # self.driver.find_element_by_xpath("//button[@class='btn btn-primary' and contains(@onclick,'Magnus Resistant Sunscreen SPF-30')]").click()
                  # time.sleep(5)
                  # self.driver.find_element_by_xpath("//button[@class='btn btn-primary' and contains(@onclick,'Vladimir Sun Expert SPF-30')]").click()
                  # time.sleep(5)
                  # self.driver.find_element_by_xpath("//button[@class='thin-text nav-link' and contains(@onclick,'goToCart')]").click()
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
                  # self.driver.find_element_by_xpath("//button[@class='btn btn-primary' and contains(@onclick,'Vassily Aloe Attack')]").click()
                  # time.sleep(5)
                  # self.driver.find_element_by_xpath("//button[@class='btn btn-primary' and contains(@onclick,'Boris Almond and Honey')]").click()
                  # time.sleep(5)
                  # self.driver.find_element_by_xpath("//button[@class='btn btn-primary' and contains(@onclick,'Wilhelm Aloe Hydration Lotion')]").click()
                  # time.sleep(5)
                  # self.driver.find_element_by_xpath("//button[@class='btn btn-primary' and contains(@onclick,'Tigran Aloe Isolani')]").click()
                  # time.sleep(5)
                  # self.driver.find_element_by_xpath("//button[@class='btn btn-primary' and contains(@onclick,'Mikhail Almond and Talc')]").click()
                  # time.sleep(5)
                  # self.driver.find_element_by_xpath("//button[@class='btn btn-primary' and contains(@onclick,'Emmanuel Aloe Vera Beauty Gel')]").click()
                  # time.sleep(5)
                  # self.driver.find_element_by_xpath("//button[@class='thin-text nav-link' and contains(@onclick,'goToCart')]").click()
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
    
    
        


    



