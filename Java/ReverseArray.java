import java.util.Scanner;

public class ReverseArray
{
    private static Scanner sc=new Scanner(System.in);
    public static void main(String[] args) {

        System.out.println("Enter count");
        int count=sc.nextInt();
        int a[]=new int[count];
        System.out.println("Enter the elements");
        for(int i=0;i<count;i++){
            a[i]=sc.nextInt();
        }
        System.out.println("Before reverse");
        for(int i=0;i<count;i++){
            System.out.print(a[i] +" ");
        }
        System.out.println("");
        reverse(a);
        System.out.println("After reverse");
        for(int i=0;i<count;i++){
            System.out.print(a[i] +" ");
        }

    }

    private static void reverse(int array[])
    {
        int n=array.length;
        int rev[]=array.clone();
        for(int i=0;i<n;i++)
        {
            array[i]=rev[n-i-1];
        }
    }
}
