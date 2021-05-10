#!/usr/bin/env python3

import logging
from commands import hello
from commands import peace
from commands import mail


def main():
    logging.basicConfig(filename='app.log', level=logging.INFO)
    logging.info('Started')
    logging.info('I told you so')
    mail()


if __name__ == "__main__":
    main()