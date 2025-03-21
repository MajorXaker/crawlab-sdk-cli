import os
import unittest
from argparse import Namespace

from cli.cli_actions.login import cli_login
from cli.cli_actions.migrate import cli_migrate
from client import get_api_address


class CliActionMigrateTestCase(unittest.TestCase):
    endpoint = get_api_address()

    def test_migrate(self):
        cli_login(Namespace(
            username='admin',
            password='admin',
            api_address=self.endpoint,
        ))
        cli_migrate(Namespace(
            api_address=get_api_address(),
            mongo_host='localhost',
            mongo_port=37017,
            mongo_db='crawlab_test',
            mongo_username=None,
            mongo_password=None,
            mongo_auth_source='admin',
        ))


if __name__ == '__main__':
    unittest.main()
