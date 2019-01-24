import java.io.*;
import java.util.*;
import java.lang.*;

public class StringArray {

    public static void main(String[] args) {
        int j;
        String x;
        String a[] = new String[100];
        String b[] = new String[100];
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 0; i <= n; i++) {
            a[i] = sc.nextLine();


        }
        for (int i = 0; i <= n; i++)
        {
            for (int k = 0; k <= a[i].length(); k++)
            {
                if (k % 2 == 0 || k == 0)
                {
                    System.out.println(a[i].charAt(k));
                }
            }
        }
    }
}