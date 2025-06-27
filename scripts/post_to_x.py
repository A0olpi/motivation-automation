import os
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Load content
with open('content.json', 'r') as f:
    content = json.load(f)

# Set up headless browser
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set up driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try:
    # Login to X
    driver.get("https://twitter.com/i/flow/login")
    time.sleep(5)  # Wait for page to load
    
    # Enter username
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[autocomplete='username']"))
    )
    username_input.send_keys(os.environ.get('X_USERNAME'))
    
    # Click Next
    next_button = driver.find_element(By.XPATH, "//span[text()='Next']")
    next_button.click()
    time.sleep(2)
    
    # Enter password
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='password']"))
    )
    password_input.send_keys(os.environ.get('X_PASSWORD'))
    
    # Click Login
    login_button = driver.find_element(By.XPATH, "//span[text()='Log in']")
    login_button.click()
    time.sleep(5)
    
    # Navigate to home
    driver.get("https://twitter.com/home")
    time.sleep(3)
    
    # Click on tweet compose box
    tweet_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div[aria-label='Tweet text']"))
    )
    tweet_box.click()
    
    # Enter tweet content
    tweet_box.send_keys(content['full_post'])
    time.sleep(1)
    
    # Click tweet button
    tweet_button = driver.find_element(By.XPATH, "//span[text()='Tweet']")
    tweet_button.click()
    
    print("Successfully posted to X")
    
except Exception as e:
    print(f"Error posting to X: {e}")
    
finally:
    driver.quit()
