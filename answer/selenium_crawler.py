# -*- coding: utf-8 -*-

import configparser
import logging
import os
from logging import DEBUG, StreamHandler, getLogger
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

logger = getLogger(__name__)
handler = StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s: %(message)s', datefmt='%Y/%m/%d %I:%M:%S'))
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False


def path(file_name):
    return os.path.normpath(os.path.join(os.path.abspath('__file__'), '../{}'.format(file_name)))


def crawler(config):
    try:
        driver = webdriver.Chrome(desired_capabilities=DesiredCapabilities.CHROME)
        driver.implicitly_wait(30)
        driver.set_page_load_timeout(30)

        url = config.get('general', 'url')
        logger.debug("access {}".format(url))
        driver.get(url)
        sleep(1)

        user_id = config.get('general', 'user_id')
        logger.debug("input user_id ".format(user_id))
        user = driver.find_element_by_xpath('//*[@id="id_username"]')
        user.send_keys(user_id)
        sleep(1)

        pass_ = config.get('general', 'password')
        logger.debug("input password ".format(pass_))
        pass_ = driver.find_element_by_xpath('//*[@id="id_password"]')
        pass_.send_keys(pass_)
        sleep(3)

        logger.debug("clicked login button")
        driver.find_element_by_xpath('//*[@id="login-form"]/div[2]/input').click()
        sleep(3)
        logger.debug("clicked ユーザ")
        driver.find_element_by_xpath('//*[@id="side-panel"]/div[1]/ul/li[1]/ul/li[1]/a').click()
        sleep(3)
        logger.debug("")

    except Exception as e:
        logger.debug(e)


def main():
    config = configparser.SafeConfigParser()
    config.read(path('selenium_crawler.conf'))
    crawler(config)


if __name__ == '__main__':
    main()
