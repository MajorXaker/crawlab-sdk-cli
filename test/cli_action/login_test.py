import os
import unittest
from argparse import Namespace

from cli.actions.login import cli_login
from client import get_api_address
from config.config import config


class CliActionLoginTestCase(unittest.TestCase):
    @staticmethod
    def test_login():
        args = Namespace(
            username='admin',
            password='admin',
            api_address=get_api_address(),
        )
        cli_login(args)
        assert os.path.exists(config.json_path)
        assert len(config.data.get('token')) > 0


if __name__ == '__main__':
    unittest.main()
