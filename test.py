import unittest
import flask
import travis_sample
from travis_sample import app


class TestIndexView(unittest.TestCase):
    def test_it_runs(self):
        with app.test_request_context("/"):
            result = travis_sample.index()
            self.assertIn("travis", result.lower())

if __name__ == "__main__":
    unittest.main()
