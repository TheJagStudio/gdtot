import pickle
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import threading
a = []
with open("url.txt") as file:
    for line in file:
      a.append(line.rstrip())
def scrapper(start):
	for i in range(start,len(a),4):
		try:
			chrome_options = Options()
	    #chrome_options.add_argument('--headless')
			chrome_options.add_argument('--no-sandbox')
			chrome_options.add_argument('--disable-dev-shm-usage')
			url = a[i]
			driver = webdriver.Chrome(options=chrome_options)
			driver.get(url)
			cookies =  pickle.load(open("./static/cookies.pkl", "rb"))
			for cookie in cookies :
			    driver.add_cookie(cookie)
			m = driver.find_element(By.ID,'down1')
			m.click()
			driver.get(url)
			for cookie in cookies :
			    driver.add_cookie(cookie)
			url = url.split("file/")[0]+"dld?id="+url.split("file/")[1]
			driver.get(url)
			time.sleep(1)
			driver.close()
			driver.quit()
			print(a[i]+" : done")
		except:
			pass
  
t1 = threading.Thread(target=scrapper, args=(1,))
t2 = threading.Thread(target=scrapper, args=(2,))
t3 = threading.Thread(target=scrapper, args=(3,))
t4 = threading.Thread(target=scrapper, args=(4,))
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
print("all done...")