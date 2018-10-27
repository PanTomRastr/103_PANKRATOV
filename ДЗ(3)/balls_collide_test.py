from unittest import (TestCase, main)
from balls_collide import *


class Tester(TestCase):
    def test_1(self):
        self.assertFalse(balls_collide((5.5, 2.4, 8.0), (5.0, 5.7, 2.0)))

    def test_2(self):
        self.assertTrue(balls_collide((10.5, 6.7, 6.7), (3.5, 2.1, 1.3)))

    def test_3(self):
        self.assertTrue(balls_collide((8.3, 5.7, 4.9), (4.1, 0.7, 1.1)))

    def test_4(self):
        self.assertTrue(balls_collide((7.1, 9.5, 0.0), (7.1, 9.5, 0.0)))

    def test_5(self):
        self.assertRaises(ValueError, balls_collide, (5.5, 2.4, 8.0), (5.0, 5.7, -2.0))


main()
