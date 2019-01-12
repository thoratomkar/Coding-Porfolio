
import java.util.HashSet;


public class find_duplicate_number
{
    // function to find duplicate number in java using hash set
      public static int findDuplicate(int[] nums)
    {
        int x=0;
        HashSet s=new HashSet<Integer>();
        for(int i=0;i<nums.length;i++)
        {
            if(s.contains(nums[i])) {
                x= nums[i];
                break;
            }
                else
                s.add(nums[i]);

        }
        return x;
    }

    public static void main(String[] args)
    {
        int a[]={2,1,3,4,5,6,2};
        System.out.println(findDuplicate(a));
    }
}

