import pickle
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://new2.gdtot.sbs/file/3320291588")
waiter = input("wait...")
pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
print(driver.get_cookies())