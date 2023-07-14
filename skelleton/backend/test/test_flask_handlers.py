import sys
sys.path.append("backend/src")

import unittest

from main import app
from main import ar

class TestFlaskHandlers(unittest.TestCase):
    def setUp(self):
        ar.clear()
        app.config.update({
        "TESTING": True,
        })

        self.client = app.test_client()

    def testExmaple(self):
        self.assertEqual(1, 1)
