import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import json

# Load cookies from JSON file and paste below, make sure you are changing true: True, false: False, null: None 👍🏻
# cookies = [
#     {
#         "domain": ".chatgpt.com",
#         "expirationDate": 1744887397.597566,
#         "hostOnly": False, 
#         "httpOnly": True,
#         "name": "__Secure-next-auth.session-token",
#         "path": "/",
#         "sameSite": "lax",
#         "secure": True,
#         "session": False,
#         "storeId": None,
#         "value": "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..MbVI1nk3L-GrCcli.fiMRLKDIj0KKsD7YNR5KLPFgT7ZRZ....."},
#     ...
# ]

# or
# Load cookies from JSON file
with open('mycookie.json', 'r') as file:
    cookies = json.load(file)

# Start the browser
options = uc.ChromeOptions()
browser = uc.Chrome(options=options)


# Just For Security Purpose :)
options.add_argument("proxy-server=200.174.198.86:8888") # You can remove this line if you don't want to use proxy

browser.get("https://chatgpt.com/")
time.sleep(2)

# Add each cookie
for cookie in cookies:
    cookie_data = {
        'name': cookie['name'],
        'value': cookie['value'],
        'domain': cookie['domain'],
        'path': cookie['path'],
        'secure': cookie['secure'],
    }

    # Add 'expiry' if available
    if 'expirationDate' in cookie:
        cookie_data['expiry'] = int(cookie['expirationDate'])

    try:
        browser.add_cookie(cookie_data)
        print(f"Added cookie: {cookie['name']}")
    except Exception as e:
        print(f"Error adding cookie {cookie['name']}: {e}")

# Refresh to apply cookies
browser.refresh()
time.sleep(2)

# Main part start from here 
# List of Multiple Question
list = [
    "Give answer of blockchain subjet questions in very short Q1. Attempt the following (Any 4): a. Explain the concept of UTXO model of Bitcoin. b. Differentiate between hot and cold wallets c. Explain mining pool and its difficulty. d. Compare and contrast private and public blockchain. e. List and explain various types of nodes used in ethereum.",
    "Which is greater: 9.9 or 9.11?",
    "Is it Ok If I created a GhatGPT Automation using Selenium or not?"
]

post = 0
for i in range(len(list)):
    browser.find_element(By.CSS_SELECTOR, "#prompt-textarea > p").send_keys(list[i])

    submit = "#composer-background > div.flex.h-\[44px\].items-center.justify-between > div:nth-child(2) > div > button > svg > path"
    WebDriverWait(browser, 100).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, submit)))
    browser.find_element(By.CSS_SELECTOR, submit).click()
    
    responce = f'/html/body/div[1]/div[2]/main/div[1]/div[1]/div/div/div/div/article[{post+2}]/div/div/div[2]/div/div[1]/div/div/div'

    endpath = f"/html/body/div[1]/div[2]/main/div[1]/div[1]/div/div/div/div/article[{post+2}]/div/div/div[2]/div/div[2]/div/div"
    post += 2
    
    time.sleep(2)
    WebDriverWait(browser, 100).until(
            EC.visibility_of_element_located((By.XPATH, endpath)))

    time.sleep(2)
    response = browser.find_element(By.XPATH, responce).text
    print(response)

    with open(f"chatgpt_response{i+1}.txt", "w", encoding="utf-8") as file:
        file.write(response)
    

time.sleep(5)
browser.quit()