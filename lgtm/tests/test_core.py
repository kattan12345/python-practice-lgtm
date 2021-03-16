import os
import sys
import unittest

sys.path.append(os.path.abspath('..'))


class LgtmTest(unittest.TestCase):
    def test_lgtm(self):
        from core import lgtm
        self.assertIsNone(lgtm())