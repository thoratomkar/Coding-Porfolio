import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution3rdMax
{
    public static void main(String[] args) {
        SolutionReal s=new SolutionReal();
        int a[]=new int[5];
        a[0]=1;
        a[1]=2;
        a[2]=3;
        a[3]=3;
        a[4]=1;
        int x=s.thirdMax(a);
        System.out.println(x);
    }

}


class SolutionReal
{
    public int thirdMax(int[] nums)
    {
        if(nums.length == 0) return 0;
        Arrays.sort(nums);
        int myIndex = 0;
        List<Integer> myList = new ArrayList<>();
        myList.add(nums[0]);
        for(int i = 0; i < nums.length; i++){
            if(nums[i] != myList.get(myIndex)){
                myList.add(nums[i]);
                myIndex++;
            }
        }
        if(myList.size()<3){
            return myList.get(myList.size()-1);
        }
        else
            return myList.get(myList.size()-3);
    }
}
