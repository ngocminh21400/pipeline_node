from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


options = Options()
options.headless = True
driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver',options=options)
driver.get('http://google.com/')
# driver.find_element(By.NAME, "q").send_keys("ming")
# driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
#driver.close()
#wait = WebDriverWait( driver, 5 )

assert driver.title == "Google"
print('DONE')

#assertEqual(driver.title == "Google")