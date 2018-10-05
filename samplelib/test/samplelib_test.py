import unittest

from samplelib import sampler


class TestSample(unittest.TestCase):

    def test_sampler(self):
        sampler.sample_function()


if __name__ == '__main__':
    unittest.main()
