


from selenium import webdriver
from page_objects import PageFactory
import conf.locators_conf as locators
# from utils.Wrapit import Wrapit
# from page_objects.Base_Page import Base_Page
import re
import time

class weathershopper_tests():

    product_price_element = locators.product_price_element
    product_add_element = locators.product_add_element
    product_category = []    
    product_moisturizers_category = []
    product_sunscreens_category = []

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

    def process_selected_products(self,product_category):
        "Process the selected products"        
        result_flag = self.add_products(product_category)
        result_flag &= self.click_cart()
        result_flag &= self.check_redirect_cart()
        
        return result_flag

    def select_product_type(self,product_moisturizers_category,product_sunscreens_category):
        "Select products type"
        title = self.get_title() 
        title = title.decode('utf-8')       
        result_flag = None    
        if title in "Moisturizers":           
            result_flag = self.process_selected_products(product_moisturizers_category)            
        elif title in 'Sunscreens':            
            result_flag = self.process_selected_products(product_sunscreens_category)               

        return result_flag   

    def click_cart(self):
        "Click on the Cart button"
        result_flag = self.click_element(self.cart_button)
        # self.conditional_write(result_flag,
            # positive='Clicked on the "cart" button',
            # negative='Failed to click on "cart" button',
            # level='debug')

        return result_flag     

    def check_redirect_cart(self):
        "Check if we have been redirected to the redirect page"
        result_flag = False        
        #self.driver.title = "The best sunscreens in the world!"
        #remove after Arun changes the title for sunscreens      
            
        result_flag = True if self.check_element_present(self.checkout_heading) else False        
        # self.conditional_write(result_flag,
                               # positive="User is redirected to cart Page ",
                               # negative="User is not redirected to cart Page",
                               # level='debug')
        if result_flag == True:
            self.switch_page("cart")

        return result_flag 
    def switch_page(self,page_name):
        "Switch the underlying class to the required Page"
        self.__class__ = PageFactory.PageFactory.get_page_object(page_name,base_url=self.base_url).__class__     

    def check_element_present(self,locator):
        "This method checks if the web element is present in page or not and returns True or False accordingly"
        result_flag = False
        if self.get_element(locator,verbose_flag=False) is not None:
            result_flag = True
        
        return result_flag

    def get_element(self,locator,verbose_flag=True):
        "Return the DOM element of the path or 'None' if the element is not found "
        dom_element = None
        try:            
            locator = self.split_locator(locator)            
            dom_element = self.driver.find_element(*locator)            
        except Exception as e:            
            # if verbose_flag is True:
                # self.write(str(e),'debug')
                # self.write("Check your locator-'%s,%s' in the conf/locators.conf file" %(locator[0],locator[1]))
            # self.exceptions.append("Check your locator-'%s,%s' in the conf/locators.conf file" %(locator[0],locator[1]))
            print(e)    
        return dom_element
    def tearDown(self):
        self.driver.quit()

   

if __name__ == "__main__":
    
    weather=weathershopper_tests()
    weather.setUp()
    weather.buy_item()
    weather.add_products()
    weather.tearDown()
    
    
        


    



