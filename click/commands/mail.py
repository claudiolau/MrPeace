#!/usr/bin/env python3

import smtplib
import click


@click.command()
def mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("claudio.lau12@gmail.com", "Varia925")
    server.sendmail("claudio.lau12@gmail.com", "claudio.lau12@gmail.com",
                    "this message is from python")
    server.quit()


if __name__ == '__main__':
    mail()
