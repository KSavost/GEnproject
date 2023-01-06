from selenium import webdriver
from selenium.common import ElementNotInteractableException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
import time


a = webdriver.Firefox()
a.get('http://os.fipi.ru/tasks/1/a%27')
time.sleep(1)
c = a.find_element(By.XPATH, "//div[@class='page-size-button']")
c.click()
time.sleep(2)

d = []
cc = a.find_elements(By.CLASS_NAME, "info-button")
for i in cc:
    i.click()

ccc = a.find_elements(By.XPATH, "//td[@class='param-row']//div")
for i in ccc:
    d.append(i.text)

print(d)

aa = a.find_elements(By.XPATH, "//body[@class='custom-scroll-no inner-answers noselect test']")
print(aa)
for i in aa:
    i.click()
    
