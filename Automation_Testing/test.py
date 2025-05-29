from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Create a Service object with the correct path to chromedriver
service = Service('/usr/local/bin/chromedriver')  # Adjust the path if needed

# Initialize WebDriver using the Service object
chrome_browser = webdriver.Chrome(service=service)

print(chrome_browser)
