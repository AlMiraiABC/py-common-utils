from unittest import TestCase
from al_utils.console import *


class TestColoredConsole(TestCase):
    """
    Should be tested by human in output console.
    These tests only for coverage.

    All colored text may not expected in vscode output panel.

    Run `python console.py` directly to see output colors.
    """

    def test_set_unset(self):
        ColoredConsole.set(color=TextColor.RED)
        print('text with color.')
        ColoredConsole.unset()

    def test_debug(self):
        ColoredConsole.debug('This is a debug.')

    def test_success(self):
        ColoredConsole.success('This is a success.')

    def test_warn(self):
        ColoredConsole.warn('This is a warning.')

    def test_error(self):
        ColoredConsole.error('This is a error.')
