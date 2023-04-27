"""
This module defines the redbubble_upload function to automate the upload of stickers to Redbubble using Selenium.
"""

import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def redbubble_upload():
    """
    This function automates the upload of stickers to Redbubble using Selenium.
    It sets up the Chrome browser options, opens a Chrome browser window, and navigates to the Redbubble homepage.
    The function then waits for 10 seconds before closing the browser window.

    Args:
        None

    Returns:
        None
    """
    ## Setup chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("user-data-dir=" + os.environ.get("ENV_CHROME_PROFILE"))

    # Ensure GUI is off
    # chrome_options.add_argument("--headless")

    # Prevent sandbox issues
    chrome_options.add_argument("--no-sandbox")

    # Set path to chromedriver as per your configuration
    homedir = os.path.expanduser("~")
    webdriver_service = Service(f"{homedir}/chromedriver/stable/chromedriver")

    # Choose Chrome Browser
    browser = webdriver.Chrome(service=webdriver_service, chrome_options=chrome_options)

    # Navigate to Redbubble website
    browser.get("https://www.remove.bg/")

    # Wait for 10 seconds
    time.sleep(1000)

    # Quit browser
    browser.quit()


if __name__ == "__main__":
    redbubble_upload()
