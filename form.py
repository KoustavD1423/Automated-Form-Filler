from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


driver_path = 'C:\\Users\\koust\\Downloads\\chromedriver-win64\\chromedriver.exe'  

chrome_options = Options()


service = ChromeService(executable_path=driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)


form_url = 'https://forms.gle/WT68aV5UnPajeoSc8'

try:
   
    driver.get(form_url)
    
   
    time.sleep(2)


    name_field = driver.find_element(By.XPATH, '//input[@aria-labelledby="i1"]')
    name_field.send_keys('Koustav Das')

    name_field = driver.find_element(By.XPATH, '//input[@aria-labelledby="i5"]')
    name_field.send_keys('9064040128')
    
    name_field = driver.find_element(By.XPATH, '//input[@aria-labelledby="i9"]')
    name_field.send_keys('koustavsamurai410@gmail.com')
    

    name_field = driver.find_element(By.XPATH, '//textarea[@aria-labelledby="i13"]')
    name_field.send_keys('Manik Para, Krishnagar, Nadia')

    name_field = driver.find_element(By.XPATH, '//input[@aria-labelledby="i17"]')
    name_field.send_keys('741101')

    name_field = driver.find_element(By.XPATH, '//input[@aria-labelledby="i25"]')
    name_field.send_keys('23-08-2000')

    name_field = driver.find_element(By.XPATH, '//input[@aria-labelledby="i26"]')
    name_field.send_keys('Male') 

    name_field = driver.find_element(By.XPATH, '//input[@aria-labelledby="i30"]')
    name_field.send_keys('GNFPYC') 



    
    submit_button = driver.find_element(By.XPATH, '//span[text()="Submit"]')
    submit_button.click()

 
    time.sleep(2)

   
    driver.save_screenshot('confirmation_page.png')

finally:
    
    driver.quit()
