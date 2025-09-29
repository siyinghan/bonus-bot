"""
Get the daily bonus.
"""
import logging

from get_daily_bonus import get_hifini, get_baidu_tb, get_baidu_baike, get_ttg, get_zmpt

if __name__ == "__main__":
    # get_hifini()
    get_zmpt()
    get_ttg()
    get_baidu_tb()
    get_baidu_baike()
    logging.info("Done!")
