"""
Get the daily bonus.
"""
import logging

from get_daily_bonus import get_hifini, get_hai_tang, get_baidu_tb, get_baidu_baike

if __name__ == "__main__":
    get_hifini()
    get_hai_tang()
    get_baidu_tb()
    get_baidu_baike()
    logging.info("Done!")
