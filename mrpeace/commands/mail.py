#!/usr/bin/env python3

import smtplib
import click


@click.command()
@click.option("--account", prompt="Your account", help="Provide your account")
@click.option("-password",
              prompt="Your password",
              help="Provide your password")
def mail(account, password):
    click.confirm('Do you want to continue?', abort=True)
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(account, password)
    server.sendmail(account, account, "this message is from python")
    server.quit()
