import java.util.*;
public class Program
{
	public static void main(String[] args) {
	    int enter;
        Scanner in = new Scanner(System.in);
        
        System.out.println("Enter percentage of your discount");
        enter = in.nextInt();
		
		System.out.print(sum(enter));
	}
    private static Object sum(int enter) {
	    int a = 0;
	    int b = 0;
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
