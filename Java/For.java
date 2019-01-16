// implementing for loop to calculate interest  


import java.util.*;
public class For
{
    public static void main(String[]args)

    {
     Scanner sc=new Scanner(System.in);
     boolean x;
     int count=0;
     for(int i=8;i>=7;i--)
     {
         System.out.println("10000 at "+i+"% interest ="+ String.format("%.2f",calculateInterest(10000,i)));
     }

     for(int i=10;i<=50;i++)
     {

         x=isPrime(i);
         if(count==10)
             break;
         if(x)
         {
             System.out.println(i+" is a prime number");
             count++;
         }

     }

    }
    public static double calculateInterest(double amount,double InterestRate)
    {
    return(amount*(InterestRate/100));
    }
    public static boolean isPrime(int n)
    {
       if(n==1)
           return false;
       for(int i=2;i<=n/2;i++)
       {
          if(n%i==0)
             return false;
       }
        return true;

    }
}
