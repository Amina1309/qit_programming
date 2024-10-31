import unittest

from AsteroidsCollision import *


class Test(unittest.TestCase):
    def test_1(self):
        result = asteroid_collision([5, 10, -5])
        self.assertEqual(result, [5, 10])

    def test_2(self):
        result = asteroid_collision([8, -8])
        self.assertEqual(result, [])

    def test_3(self):
        result = asteroid_collision([10, 2, -5])
        self.assertEqual(result, [10])


if __name__ == '__main__':
    unittest.main()
