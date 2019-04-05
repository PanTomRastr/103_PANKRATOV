import java.util.*;
public class decimalToBinaryTest
{
   public static void main (String [] args)
   {

      int n;
      Scanner in = new Scanner(System.in);

      System.out.println("Enter a positive interger");
      n=in.nextInt();

      if(n < 0)
      {
         System.out.println("Not a positive interger");
      }

      else
      {
         System.out.print("Convert to binary is: ");
         System.out.print(binaryform(n));
      }   
   }


   private static Object binaryform(int n)
   {   int n1,i;
       String k=new String();
       String p=new String();
       
       while(n>0)
       {
         n1=n%2;
         n=n/2;
         k=k+n1;
       }
       i=k.length()-1;
      while(i>=0)
      {
          p=p+k.charAt(i);
          i--;
      }
      return p; 
   }
}
