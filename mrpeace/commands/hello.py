#!/usr/bin/env python3
import click

@click.command()
def hello():
    click.secho('MrPeace the only cli to peace!', fg='blue')
