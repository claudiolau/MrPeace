#!/usr/bin/env python3

import pytest
from click.testing import CliRunner
from mrpeace import cli


def test_notification():
    runner = CliRunner()
    result = runner.invoke(cli.hi, ["hi"])
    assert result.exception
