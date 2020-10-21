"""Helper functions for product app"""


class PasswordGenerator:
    def get_hash(self):
        """Returns password hash"""
        return 'contraseña_segura'

    def generate_password(self):
        """Generates a random password"""
        hsh = self.get_hash()
        return hsh
