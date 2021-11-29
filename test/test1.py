from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


options = Options()
options.headless = True
driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver',options=options)
driver.get('http://localhost:4000')
# driver.find_element(By.NAME, "q").send_keys("ming")
# driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
#driver.close()
#wait = WebDriverWait( driver, 5 )
# for request in driver.requests:
#     if request.response:
#         print(
#             request.url,
#             request.response.status_code,
#             request.response.headers['Content-Type']
#         )


try:
  assert driver.title == "Google"
except:
  print("NOT Google!")

print('DONE')

#assertEqual(driver.title == "Google")