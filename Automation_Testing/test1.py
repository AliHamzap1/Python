from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
 
service = Service(executable_path='/usr/local/bin/chromedriver')
 
options = Options()
options.add_experimental_option('detach', True) #this ensures chrome window does not close
 
chrome_browser = webdriver.Chrome(service=service, options=options)
 
print(chrome_browser)

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service

# url = "mitco.pk"

# service_obj = Service("/usr/local/bin/chromedriver")
# driver = webdriver.Chrome(service=service_obj)
# driver.get(url)