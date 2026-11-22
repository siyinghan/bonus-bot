"""
Utility functions.
"""
import logging
import os
import sys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

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
    user_data_dir = os.path.expanduser("~/Library/Application Support/Google/Chrome")
    options = webdriver.ChromeOptions()
    options.add_argument(f"--user-data-dir={user_data_dir}")
    options.add_argument(f"--profile-directory={profile}")
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    driver.set_window_size(1400, 1000)
    return driver
