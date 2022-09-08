import pickle
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

def get_video():
  url = "https://new.gdtot.eu/file/2858919423"
  driver = webdriver.Chrome(options=chrome_options)
  driver.get(url)
  cookies =  pickle.load(open("static/cookies.pkl", "rb"))
  for cookie in cookies :
      driver.add_cookie(cookie)
  m = driver.find_element(By.ID,'down1')
  m.click()
  driver.get(url)
  for cookie in cookies :
      driver.add_cookie(cookie)
  url = "https://new.gdtot.eu/dld?id=" + url.split("file/")[1]
  driver.get(url)
  time.sleep(1)
  driver.close()

get_video()