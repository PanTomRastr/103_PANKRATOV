from roman_logic import Roman
from unittest import TestCase, main


class Validator(TestCase):

    def test_1(self):
        self.assertEqual(Roman.do_roman_seq(37), ('XXXVII'))

    def test_2(self):
        self.assertEqual(Roman.do_roman_seq(1990), ('MCMXC'))

    def test_3(self):
        self.assertEqual(Roman.do_roman_seq(765), ('DCCLXV'))

    def test_4(self):
        self.assertEqual(Roman.do_roman_seq(381), ('CCCLXXXI'))

    def test_5(self):
        self.assertEqual(Roman.do_roman_seq(8), ('VIII'))


if __name__ == '__main__':
    main()
