from al_utils.logger import Logger
from unittest import TestCase


class TestLogger(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.logger = Logger(TestLogger.__name__).logger

    def test_info(self):
        self.logger.info('This is a info message')

    def test_error(self):
        self.logger.error('This is a error message')
