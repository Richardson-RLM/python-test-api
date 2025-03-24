import unittest
from app import create_app

class TestCPFAPI(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()

    def test_free_cpf(self):
        """Testa um CPF que não está na blacklist."""
        response = self.app.get('/12345678900')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["status"], "FREE")

    def test_block_cpf(self):
        """Testa um CPF que está na blacklist."""
        response = self.app.get('/00000000000')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["status"], "BLOCK")

if __name__ == "__main__":
    unittest.main()