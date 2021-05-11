#!/usr/bin/env python3

import os
import logging
from commands import hello
from commands import mail


def cli():
    logging.basicConfig(filename="app.log", level=logging.INFO)
    logging.info("Started")
    hello()
    mail()


if __name__ == "__main__":
    cli()
