"""
Automates the process of opening web pages to obtain daily bonuses.
This functions automatically opens the pages and clicks on the appropriate buttons to receive the bonus.
The pages to be opened are assumed to be pre-defined and saved within the function.
"""
from time import sleep

from selenium.webdriver.common.by import By

from util import logging, activate_chrome_driver

hifini_url = "https://www.hifini.com"
zmpt_url = "https://zmpt.cc/torrents.php"
ttg_url = "https://totheglory.im/browse.php?c=M"
baidu_tb_url = "https://tieba.baidu.com/f?kw=%B9%A8%BF%A1"
baidu_baike_url = "https://baike.baidu.com/item/%E9%BE%9A%E4%BF%8A/19919509"


def get_hifini():
    """
    Automates the process of logging in to the HiFiNi website and obtaining the daily bonus.
    """
    with activate_chrome_driver("Default") as driver:
        driver.get(hifini_url)
        logging.info(f"Open HiFiNi: {hifini_url}")
        driver.find_element(by=By.XPATH, value='//*[@id="sign"]').click()
        logging.info("Click to get the daily bonus from HiFiNi")
        sleep(2)


def get_zmpt():
    """
    Automates the process of logging in to the ZmPT website and obtaining the daily bonus.
    """
    with activate_chrome_driver("Default") as driver:
        driver.get(zmpt_url)
        logging.info(f"Open ToTheGlory: {zmpt_url}")
        sleep(1)
        driver.find_element(by=By.XPATH,
                            value='//*[@id="info_block"]/tbody/tr/td/table/tbody/tr/td[1]/span/a[1]').click()
        logging.info("Click to get the daily bonus from ZmPT")
        sleep(2)


def get_ttg():
    """
    Automates the process of logging in to the ToTheGlory website and obtaining the daily bonus.
    """
    with activate_chrome_driver("Default") as driver:
        driver.get(ttg_url)
        logging.info(f"Open ToTheGlory: {ttg_url}")
        sleep(1)
        driver.find_element(by=By.XPATH, value='//*[@id="signed"]').click()
        logging.info("Click to get the daily bonus from ToTheGlory")
        sleep(2)


def get_baidu_tb():
    """
    Automates the process of logging in to the Baidu Tieba website and obtaining the daily bonus.
    """
    with activate_chrome_driver("Default") as driver:
        driver.get(baidu_tb_url)
        logging.info(f"Open Baidu Tieba: {baidu_tb_url}")
        # click twice to make sure of getting the bonus
        xpath = '//*[@id="signstar_wrapper"]/a'
        driver.find_element(by=By.XPATH, value=xpath).click()
        sleep(1)
        driver.find_element(by=By.XPATH, value=xpath).click()
        logging.info("Click to get the daily bonus from Baidu Tieba")
        sleep(2)


def get_baidu_baike():
    """
    Automates the process of logging in to the Baidu Baike website and obtaining the daily bonus.
    """
    with activate_chrome_driver("Default") as driver:
        driver.get(baidu_baike_url)
        logging.info(f"Open Baidu Baike: {baidu_baike_url}")
        sleep(4)
        for i in range(3):
            driver.find_element(by=By.XPATH,
                                value='//*[@id="J-lemma-main-wrapper"]/div[1]/div/div/div/div[2]/div[4]/div[1]/div[1]/div[1]').click()
            logging.info(f"{i + 1} click to get the daily bonus from Baidu Baike")
            sleep(5)
