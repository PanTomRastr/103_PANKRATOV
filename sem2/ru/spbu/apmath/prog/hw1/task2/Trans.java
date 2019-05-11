public class Trans {
        static String thousand = "тысяча";
        static String[] hundreds = {"","сто","двести","триста","четыреста","пятьсот","шестьсот","семьсот","восемьсот","девятьсот"};
        static String[] tens = {"","","двадцать","тридцать","сорок","пятьдесят","шестьделят","семьдесят","восемьдесят","девятьсот"};
        static String[] normal = {"","один","два","три","четыре","пять","шесть","семь","восемь","девять","десять","одиннадцать","двенадцать","тринадцать","четырнадцать","пятнадцать","шестнадцать","семнадцать","восемнадцать","девятнадцать"};
        public static String trans(int number){
            String line;
            line = "";
            if (number / 1000 == 1){
                line = line + thousand;
                number = number % 1000;
            }
            line = line + hundreds[number / 100];
            number = number % 100;
            if (number > 19){
                line = line + tens[number / 10];
                number = number % 10;
            }
            line = line + normal[number];
            return line;
        }

    }
