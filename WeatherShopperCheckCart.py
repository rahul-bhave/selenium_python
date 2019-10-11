import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# from utils.BrowserStack_Library import BrowserStack_Library

class weathershopper_tests():

    #iframe_name = "//iframe[@name='stripe_checkout_app']"
    #msg_list = []

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
                  self.driver.find_element_by_xpath("//button[@class='thin-text nav-link' and contains(@onclick,'goToCart')]").click()

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
                  self.driver.find_element_by_xpath("//button[@class='thin-text nav-link' and contains(@onclick,'goToCart')]").click()
               else:
                  print("You are on wrong page")
    
    


        except Exception as e:
            print(e)

    def check_cart(self):
        
        
        
        try:
            
            table=self.driver.find_element_by_xpath("//table[@class='table table-striped']")
            rows = table.find_elements_by_xpath("//tbody/descendant::tr")
            
            result_data = []
            # Go to each row and get the no of columns and the navigate to column 
            # Then get the text from each column
            for i in range(0,len(rows)):
            # Find no of columns by getting the td elements in each row
                cols = rows[i].find_elements_by_tag_name('td')
                cols_data = []
                for j in range(0,len(cols)):
                   # Get the text of each field 
                   cols_data.append(cols[j].text.encode('utf-8'))           
                result_data.append(cols_data)
            # Print the result list
            print(result_data)
            print(len(result_data))
            print("All items are added on cart")
            self.driver.save_screenshot("C:\\Users\\Rahul Bhave Qxf2\\code\\rahul-qxf2\\selenium_python\\Screenshots\\PaymentCheckCart.png")
            time.sleep(10)
            
            

        except Exception as e:
            print(e)

    

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    
    weather=weathershopper_tests()
    weather.setUp()
    weather.buy_item()
    # time.sleep(5)
    weather.check_cart()
    weather.tearDown()
  