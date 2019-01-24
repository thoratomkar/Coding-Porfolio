import java.io.*;
import java.util.*;

public class Solution4 {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int no_of=sc.nextInt();
        int i,j,sum=0,temp,count=0;
        int no[]=new int[no_of];
        for(i=0;i<no_of;i++)
        {
            no[i]=sc.nextInt();
            sum+=no[i];
        }
        int n=no.length;
        float mean=sum/i,median;
        System.out.println(mean);
        for(i=0;i<n-1;i++)
        {
            for(j=0;j<n-i-1;j++)
            {
                if (no[i] > no[i + 1])
                {
                    temp = no[i];
                    no[i] = no[i + 1];
                    no[i + 1] = temp;

                }
            }
        }
        median=(n+1)/2;
        System.out.println(median);
        int maxValue = 0, maxCount = 0;

        for (int z = 0; z < no.length; ++z) {
            int ccount = 0;
            for (int x = 0; x < no.length; ++x) {
                if (no[x] == no[z])
                    ++ccount;
            }
            if (ccount > maxCount) {
                maxCount = ccount;
                maxValue = no[z];
            }

        }
        int mode=maxValue;
        System.out.println(mode);
    }
}