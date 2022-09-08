from flask import Flask, render_template
from flask import request
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
app = Flask('')


@app.route('/')
def new():
    return "Hello world"


@app.route('/home', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        url = request.form.get('Url')
        password = request.form.get('Password')
        username = request.form.get('Username')
        #print(url,password,username)
        if username == "gdtot" and password == "allow" and url.find(
                "https://new2.gdtot") != -1:
            driver = webdriver.Chrome(options=chrome_options)
            driver.get(url)
            cookies = pickle.load(open("static/cookies.pkl", "rb"))
            for cookie in cookies:
                driver.add_cookie(cookie)
            m = driver.find_element(By.ID, 'down1')
            m.click()
            driver.get(url)
            for cookie in cookies:
                driver.add_cookie(cookie)
            url = url.split("file/")[0] + "dld?id=" + url.split("file/")[1]
            driver.get(url)
            time.sleep(1)
            driver.close()
            driver.quit()
            return render_template('input.html')
    return render_template('input.html')


app.run(debug=True, host="0.0.0.0", port=8080)
