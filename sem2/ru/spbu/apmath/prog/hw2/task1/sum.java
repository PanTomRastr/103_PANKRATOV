public class sum {
     static int Sum(int enter) {
        int a = 0;
        int b;
        while(enter > 0)
        {
            a = a + (enter % 10);
            b = enter / 10;
            enter = b;
            if (enter == 0){
                if (a >=10){
                    enter = a;
                    a = 0;
                }
            }
        }
        return a;
    }
}
