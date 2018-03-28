# -*- coding: utf-8 -*-

import argparse
import logging
import os
from logging import DEBUG, StreamHandler, getLogger

import lxml
import requests
from bs4 import BeautifulSoup

logger = getLogger(__name__)
handler = StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s: %(message)s', datefmt='%Y/%m/%d %H:%M:%S'))
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False


def main():
    try:
        parser = argparse.ArgumentParser(description='requests crawler for internal lecture')
        parser.add_argument('-u', '--url', type=str, dest='url', required=True, help='access url to want to get web-page as htlm file.')
        parser.add_argument('-f', '--filename', type=str, dest='file_name', required=True, help='filename of output file which got by requetsts access')
        args = parser.parse_args()

        headers = {
            'User-Agent': 'Mozilla / 5.0 (MacintoshIntel Mac OS X 10_12_6) AppleWebKit / 537.36 (KHTML, like Gecko) Chrome / 62.0.3202.89 Safari / 537.36'
        }
        res = requests.get("http://{}".format(args.url), headers=headers)
        logger.debug("accessed http://{}".format(args.url))

        if res.status_code == 200:
            logger.debug("succeeded access.")
            file_name = "{}/html/{}".format(os.path.dirname(os.path.abspath(__file__)), args.file_name)
            with open(file_name, "w") as f:
                logger.debug("write html data to file.")
                f.write(str(BeautifulSoup(res.text, "lxml")))
            logger.debug("finish write data.")

    except Exception as e:
        logger.debug(e)


if __name__ == '__main__':
    main()
