# -*- coding: utf-8 -*-

import argparse
import logging
import os
from logging import DEBUG, StreamHandler, getLogger

import lxml
from bs4 import BeautifulSoup

logger = getLogger(__name__)
handler = StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s: %(message)s', datefmt='%Y/%m/%d %H:%M:%S'))
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False


def tag_print(tag):
    if "href" in str(tag):
        print("tag: {}, text: {}, link: {}".format(tag.name, tag.text, tag.get("href")))
    else:
        print("tag: {}, text: {}".format(tag.name, tag.text))


def main():
    try:
        parser = argparse.ArgumentParser(description='scrayping script for internal lecture')
        parser.add_argument('-f', '--filename', type=str, dest='file_name', required=True, help='filename of input file to get some tags')
        args = parser.parse_args()

        file_name = "{}/html/{}".format(os.path.dirname(os.path.abspath(__file__)), args.file_name)
        with open(file_name, "r") as f:
            logger.debug("read html file.")
            soup = BeautifulSoup(f, "lxml")

        side_bar = soup.find(class_="nav nav-list navlist-menu-level-0")
        for tag in side_bar.find_all("a"):
            tag_print(tag)

        container = soup.find(class_="col-md-7 middle")
        tag_print(container.find("h2"))
        tag_print(container.find("p"))
        for tag in container.find_all("a"):
            tag_print(tag)
        logger.debug("finished scrayping.")

    except Exception as e:
        logger.debug(e)


if __name__ == '__main__':
    main()
