import smile_logic as sl
from unittest import TestCase, main


class Validator(TestCase):

    def test_1(self):
        self.assertTrue(sl.smile('Hello_dear_friend'))

    def test_2(self):
        self.assertTrue(sl.smile('[3123e<ll>o 2(34)23rld]'))

    def test_3(self):
        self.assertTrue(sl.smile('[<asd>12as]'))

    def test_4(self):
        self.assertTrue(sl.smile('[[][][][][][][][][]][][][][][]'))

    def test_5(self):
        self.assertFalse(sl.smile(']Hello world['))

    def test_6(self):
        self.assertFalse(sl.smile('[[][][][][][][][][][](((('))

    def test_7(self):
        self.assertFalse(sl.smile('[[<]>[][][][][][][][][]'))


if __name__ == '__main__':
    main()
