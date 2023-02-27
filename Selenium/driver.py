## Run selenium and chrome driver to scrape data from cloudbytes.dev
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

## Setup chrome options
# chrome_options = Options()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(
    "user-data-dir=" + os.environ.get("ENV_CHROME_PROFILE")
)  # Path to your chrome profile, to find it you can open chrome and type: "chrome://version/" on URL

# chrome_options.add_argument("--headless") # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")

# Set path to chromedriver as per your configuration
homedir = os.path.expanduser("~")
webdriver_service = Service(f"{homedir}/chromedriver/stable/chromedriver")

# Choose Chrome Browser
browser = webdriver.Chrome(service=webdriver_service, chrome_options=chrome_options)


# Get page - Redbubble
browser.get("https://www.redbubble.com")

# # Extract email and password fields
# email = browser.find_element(By.ID, "ReduxFormInput1")
# password = browser.find_element(By.ID, "ReduxFormInput2")
# # login = browser.find_element(By.CLASS_NAME, "app-ui-components-Button-Button_wrapper_22Hm3 app-ui-components-LoginForm-LoginForm_button_3v_Lh")

# # Send keys to email and password fields and login
# email.send_keys(os.environ.get("ENV_REDBUBBLE_EMAIL"))
# password.send_keys(os.environ.get("ENV_REDBUBBLE_PASSWORD"))
# password.send_keys(Keys.RETURN)


# Wait for 3 seconds
time.sleep(100)
browser.quit()
