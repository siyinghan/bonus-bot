"""
Get the daily bonus.
"""
import logging

from get_daily_bonus import get_btschool, get_ttg, get_baidu_tb

if __name__ == "__main__":
    get_btschool()
    get_ttg()
    get_baidu_tb()
    logging.info("Done!")
