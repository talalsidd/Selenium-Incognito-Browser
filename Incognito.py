import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.maximize_window()
driver.get('https://google.com')
time.sleep(3)
driver.close()

        
            
          
           
            
            
            
            

            
                        
         
        

   



