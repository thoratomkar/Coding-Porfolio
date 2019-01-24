//to find majority element

import java.util.*;

class Solution {
    public static int majorityElement(int[] nums) {
        if(nums.length == 1) {
            return nums[0];
        }
        Arrays.sort(nums);
        return nums[nums.length / 2];
    }



    public static void main(String[] args) {
        int a[]={1,2,3,3,2,3};
        int x=majorityElement(a);
        System.out.println("Majority element is "+ x);

    }
    }
