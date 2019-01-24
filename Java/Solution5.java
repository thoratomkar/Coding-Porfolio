class Solution5 {
    public int searchInsert(int[] nums, int target)
    {
        int n=nums.length;
        int result=0;
        for(int i=0;i<=n-1;i++)
        {
            if(nums[i]==target)
            {  result=i; }
            if(target>nums[i])
            {
                result=i+1;
            }
            else
            {
                return i;
            }
        }
        return result;

    }

    public static void main(String[] args)
    {
        Solution5 s=new Solution5();
        int nums[]={4,6,7,8};
        System.out.println(s.searchInsert(nums,9));
    }
}