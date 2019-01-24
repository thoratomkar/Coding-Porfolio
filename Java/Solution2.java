import java.io.*;
import java.util.*;

public class Solution2 {

    public static void main(String[] args)
    {

        Scanner sc=new Scanner(System.in);
        int i,n,zero=0,x;
        x=sc.nextInt();

        // Initialize result
        int count = 0;

        // Count the number of iterations to
        // reach x = 0.
        while (x!=0)
        {
            // This operation reduces length
            // of every sequence of 1s by one.
            x = (x & (x << 1));

            count++;
        }

        System.out.println(count);
    }
}