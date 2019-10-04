# a) Open  https://weathershopper.pythonanywhere.com in your browser

import time
from selenium import webdriver
driver=webdriver.Chrome()

driver.get('https://weathershopper.pythonanywhere.com')
driver.maximize_window()
time.sleep(3)

# Check if the title of the page is proper
if(driver.title=="The best moisturizers in the world!"):
    print ("Success: The best moisturizers in the world!")
else:
    print ("Failed: Title is incorrect") 

# read the temprature
# temp=driver.find_element_by_xpath("//div[@id='weather']")
temp=driver.find_element_by_xpath("//span[@id='temperature']")
print("The temperature is %s"%temp.text)
print("The temperature in bytes is %s"%temp.text.encode('utf-8'))

#temp_text=driver.find_element_by_xpath("//span[@id='temperature']")
# print(temp_text)
# val=temp_text.get_attribute("text")
# print(val)

# attribute_value = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "temperature"))).get_attribute("attribute_name")

# if temp is greater than 30 then go for sunscreens

if (temp.text.encode('utf8'))>= bytes('20','utf-8'):
   driver.find_element_by_xpath("//button[@class='btn btn-primary' and text()='Buy sunscreens']").click()
   is_screen_visible=driver.find_element_by_xpath("//h2[contains(text(),'Sunscreens')]")
   if is_screen_visible.is_displayed():
      print("You are on Buy Sunscreens page")
      driver.find_element_by_xpath("//button[@class='btn btn-primary' and contains(@onclick,'Robert Herbals Sunblock SPF-40')]").click()
      driver.find_element_by_xpath("//button[@class='thin-text nav-link' and contains(@onclick,'goToCart')]").click()
      is_screen_visible=driver.find_element_by_xpath("//div[@class='row justify-content-center' and h2='Checkout']//following-sibling::div[@class='row justify-content-center top-space-50' ]/descendant::td[contains(text(),'Robert Herbals Sunblock SPF-40')]")
      print("Suncsreen added-Robert Herbals Sunblock SPF-40")
   else:
      print("You are on wrong page")
      
else:
    driver.find_element_by_xpath("//button[@class='btn btn-primary' and text()='Buy moisturizers']").click()
    is_screen_visible=driver.find_element_by_xpath("//h2[contains(text(),'Moisturizers')]")
    if is_screen_visible.is_displayed():
      print("You are on Buy Moisturizers page")
    else:
      print("You are on wrong page")


# Quit the browser window
driver.close()

# Adding sunscreens:


    



