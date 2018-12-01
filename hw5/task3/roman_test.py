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

    def test_6(self):
        self.assertEqual(Roman(34)+Roman(1965), Roman(1999))

    def test_7(self):
        self.assertEqual(Roman(3)+Roman(165), Roman(168))

    def test_8(self):
        self.assertEqual(Roman(4)+Roman(965), Roman(969))

    def test_9(self):
        self.assertEqual(Roman(555)+Roman(1222), Roman(1777))

    def test_10(self):
        self.assertEqual(Roman.do_roman_seq(9+1999), ('Выходит из диапазона'))

    def test_11(self):
        self.assertEqual(Roman.do_roman_seq('nechislo'), ('Это не цифра!'))

    def test_12(self):
        self.assertEqual(Roman.do_roman_seq(12046), ('Выходит из диапазона'))

    def test_13(self):
        self.assertEqual(Roman.do_roman_seq('hello'), ('Это не цифра!'))

    def test_14(self):
        self.assertEqual(Roman.do_roman_seq('12'), ('XII'))

    def test_15(self):
        self.assertEqual(Roman.do_roman_seq('243'), ('CCXLIII'))

    def test_16(self):
        self.assertEqual(Roman.do_roman_seq('123'), ('CXXIII'))


if __name__ == '__main__':
    main()
