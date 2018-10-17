"""Unit test to test the app."""
from unittest import TestCase

from cfb import cli
from . import runner


class TestPrint(TestCase):
    """Unit test class to test the app."""

    def setUp(self):
        self.text = "text"

    def test_help(self):
        result = runner.invoke(cli.cli, ['--help'])
        self.assertEqual(0, result.exit_code)
        self.assertTrue("Usage" in result.output)

    def test_version(self):
        from cfb import __version__
        result = runner.invoke(cli.cli, ['--version'])
        self.assertEqual(0, result.exit_code)
        self.assertTrue(__version__ in result.output)

    def test_write(self):
        result = runner.invoke(cli.write, [self.text])
        self.assertEqual(0, result.exit_code)
        self.assertTrue(self.text in result.output)
