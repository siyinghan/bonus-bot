from time import sleep

from selenium.webdriver.common.by import By

from util import logging, activate_chrome_driver

profiles = ["Profile 2", "Profile 3", "Profile 4", "Profile 5"]
weibo_login_url = "https://weibo.com/login.php"
chaohua_url = ["https://weibo.com/p/100808873efffe1c242a61ca77f8202f8201a8",
               "https://weibo.com/p/100808de24bcab581df1e191398e39f22bc0cb",
               "https://weibo.com/p/100808d3fa73b65abd6f2e91cf143c1726319f"]


def get_bonus_from_weibo():
    for profile in profiles:
        with activate_chrome_driver(profile) as driver:
            driver.get(weibo_login_url)
            sleep(1)
            for i in range(len(chaohua_url)):
                driver.get(chaohua_url[i])
                logging.info(f"Open Weibo Chaohua: {chaohua_url[i]}")
                sleep(4)
                xpath = '//*[@id="Pl_Core_StuffHeader__1"]/div/div[2]/div/div[3]/div/div[3]/a'
                driver.find_element(by=By.XPATH, value=xpath).click()
                logging.info(f"Click to get the daily bonus from Chaohua {chaohua_url[i]}")
                sleep(2)
