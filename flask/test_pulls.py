from unittest import TestCase
import handlers.pulls as pulls
import setts

print(setts.json)


class TestPrime(TestCase):

    def setUp(self):
        """Init"""
    def test_connect(self):
        """Test for is _connect"""
        self.assertIsInstance(pulls.connect(1, 2, 3), list)

    def test_get_pulls(self):
        """Test for is _get_pulls"""
        self.assertIsInstance(pulls.get_pulls(1, 2, 3), list)

    def test_process(self):
        """Test for is _prime"""
        self.assertEqual(pulls.process(setts.json, "open"),
                         setts.json_open)
        self.assertEqual(pulls.process(setts.json, "accepted"),
                         setts.json_accepted)
        self.assertEqual(pulls.process(setts.json, "needs work"),
                         setts.json_needs_work)
        self.assertEqual(pulls.process(setts.json, "closed"),
                         setts.json_closed)

    def tearDown(self):
        """Finish"""
