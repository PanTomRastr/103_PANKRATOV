from poly_logic import poly
from unittest import TestCase, main


class Validator(TestCase):

    def test_1(self):
        app = poly()
        self.assertEqual(app.start_app('23x^3+13+18x^2-4x'), '69x^2+36x^1-4')

    def test_2(self):
        app = poly()
        self.assertEqual(app.start_app('8x-5x^8+11x^11'), '8-40x^7+121x^10')

    def test_3(self):
        app = poly()
        self.assertEqual(app.start_app('100x^1-9x^111'), '100-999x^110')

    def test_4(self):
        app = poly()
        self.assertEqual(app.start_app('x^10-13x^24+123'), '10x^9-312x^23')

    def test_5(self):
        app = poly()
        self.assertEqual(app.start_app('2x^12-18x+124'), '24x^11-18')


if __name__ == '__main__':
    main()
