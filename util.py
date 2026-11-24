"""
Utility functions.
"""
import logging
import os
import sys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Use a dedicated Chrome profile instead of the daily one, so that Chrome can
# stay open while the script runs.
CHROME_PROFILE_DIR = os.path.expanduser("~/Library/Application Support/bonus-bot/chrome-profile")

logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def activate_chrome_driver(profile):
    """
    Activate Selenium Chrome driver.
    :return: driver
    """
    options = webdriver.ChromeOptions()
    options.add_argument(f"--user-data-dir={CHROME_PROFILE_DIR}")
    options.add_argument(f"--profile-directory={profile}")
    options.add_argument("--disable-extensions")
    # Hide the automation markers, otherwise Baidu redirects to 百度安全验证.
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",
                           {"source": "Object.defineProperty(navigator,'webdriver',{get:()=>undefined})"})
    driver.set_window_size(1400, 1000)
    return driver
