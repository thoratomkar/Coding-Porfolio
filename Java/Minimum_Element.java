// program to find minimum element in java

import java.util.Scanner;

public class Minimum_Element {



    private  static Scanner sc=new Scanner(System.in);
    public static void main(String[] args)
    {
        int x;

        System.out.println("Enter count");
        x=sc.nextInt();

        int returnedArray[]=readIntegers(x);
        int small=findMin(returnedArray);
        System.out.println("The smallest element is "+small);

    }

    public static int[] readIntegers(int count)
    {
        int i;
        int x=count;
        int[] a=new int[x];
        System.out.println("Enter the numbers");
        for(i=0;i<a.length;i++)
        {
            a[i]=sc.nextInt();
        }
        return a;
    }

    public static int findMin(int a[])
    {
        int i,min=0;
        int n=a.length;
        for(i=1;i<n;i++)
        {
            if(a[i]>a[i-1])
            {
                min=a[i-1];
            }
            else
                min=a[i];

        }
        return min;
    }


}


