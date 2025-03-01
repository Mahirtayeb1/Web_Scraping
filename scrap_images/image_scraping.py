from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

path = "D:\\web scrapping Images\\chromedriver.exe"

# Create a Service object
service = Service(path)

# Initialize the WebDriver with the Service object
wd = webdriver.Chrome(service=service)

# Example usage
# wd.get("https://example.com")
# print(wd.title)

#wd.quit()