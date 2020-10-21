"""Products app example test"""

from unittest.mock import MagicMock

from django.test import SimpleTestCase

from ..helpers import PasswordGenerator


class ExampleTest(SimpleTestCase):
    """Contains unit and integration tests"""

    def test_generate_password(self):
        """Tests that password match"""
        generator = PasswordGenerator()
        generator.get_hash = MagicMock(return_value='random')

        password = generator.generate_password()
        self.assertEqual(password, 'random')
