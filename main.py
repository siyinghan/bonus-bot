"""
Open pages and check in.
"""
import logging
import sys
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

hifini_url = "https://www.hifini.com"
hai_tang_url = "https://www.lvhtebook.com/?act=signinlst"
baidu_tb_url = "https://tieba.baidu.com/f?kw=%B9%A8%BF%A1"
baidu_baike_url = "https://baike.baidu.com/item/%E9%BE%9A%E4%BF%8A/19919509"

logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def get_daily_bonus():
    """
    Auto-open pages and get the daily bonus.
    """
    with activate_chrome_driver() as driver:
        driver.get(hifini_url)
        logging.info(f"Chrome driver open HiFiNi: {hifini_url}")
        driver.find_element(by=By.XPATH, value='//*[@id="sign"]').click()
        logging.info("Click to get the daily bonus from HiFiNi")
        sleep(3)

    with activate_chrome_driver() as driver:
        driver.get(hai_tang_url)
        logging.info(f"Chrome driver open HaiTang: {hai_tang_url}")
        driver.find_element(by=By.XPATH, value='//*[@id="mypages"]/center/a[1]').click()
        logging.info("Click to get the daily bonus from HaiTang")
        sleep(3)

    with activate_chrome_driver() as driver:
        driver.get(baidu_tb_url)
        logging.info(f"Chrome driver open Baidu Tieba: {baidu_tb_url}")
        driver.find_element(by=By.XPATH, value='//*[@id="signstar_wrapper"]/a/span[1]').click()
        logging.info("Click to get the daily bonus from Baidu Tieba")
        sleep(3)

    with activate_chrome_driver() as driver:
        driver.get(baidu_baike_url)
        logging.info(f"Chrome driver open Baidu Baike: {baidu_baike_url}")

        for i in range(3):
            driver.find_element(by=By.XPATH, value='//*[@id="starFlower"]/div/em').click()
            logging.info(f"{i + 1} click to get the daily bonus from Baidu Baike")
            sleep(4)

    logging.info("Done!")


def activate_chrome_driver():
    """
    Activate Selenium Chrome driver.
    :return: driver
    """
    options = webdriver.ChromeOptions()
    options.add_argument(r"--user-data-dir=~/Library/Application Support/Google/Chrome")
    options.add_argument(rf"--profile-directory=Default")
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    driver.set_window_size(1400, 1000)
    return driver


if __name__ == "__main__":
    get_daily_bonus()
