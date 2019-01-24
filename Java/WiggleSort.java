import java.util.Arrays;

public class WiggleSort
{
    public static void main(String[] args)
    {
        int a[]={5,1,1,6,4,54,8,6};
        WiggleSort s=new WiggleSort();
        s.wiggleSort(a);
    }

    public void wiggleSort(int[] nums)
    {
        Arrays.sort(nums);
        int[] temp = new int[nums.length];
        int s = (nums.length + 1) >> 1, t = nums.length;
        for (int i = 0; i < nums.length; i++)
        {
            temp[i] = (i & 1) == 0 ?  nums[--s] : nums[--t] ;
        }

        for (int i = 0; i < nums.length; i++)
        {
            nums[i] = temp[i];
            System.out.print(nums[i]+" ");
        }
    }
}

