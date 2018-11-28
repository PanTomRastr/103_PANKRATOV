class Roman:

    def __init__(self, seq):
        self.seq = seq
        self.result = Roman.do_roman_seq(self.seq)

    def __str__(self):
        return self.result

    def __int__(self):
        return self.seq

    def __eq__(self, other):
        if isinstance(other, Roman):
            return self.seq == other.seq
        return False

    def __add__(self, other):
        if isinstance(other, Roman):
            return Roman(self.seq + other.seq)
        return TypeError("Это не Римская цифра!")

    @staticmethod
    def do_roman_seq(seq):
        try:
            int(seq)
        except ValueError:
            return("Это не цифра!")
        if int(seq) > 1999 or int(seq) < 1:
            return("Выходит из диапазона")
        else:
            str_1000 = ''
            str_100 = ''
            str_10 = ''
            str_1 = ''
            seq = int(seq)
            ones = seq % 10
            seq = seq // 10
            tenners = seq % 10
            seq = seq // 10
            weave = seq % 10
            seq = seq // 10
            millesimal = seq % 10
            o = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
            t = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
            w = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
            m = ['', 'M', 'MM']
            if millesimal != 0 and millesimal < 2:
                str_1000 = m[millesimal]
            if weave != 0:
                str_100 = w[weave]
            if tenners != 0:
                str_10 = t[tenners]
            if ones != 0:
                str_1 = o[ones]
            suq_str = str_1000 + str_100 + str_10 + str_1
            return suq_str
