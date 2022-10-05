class Solution {
    public int pivotIndex(int[] nums) {
        int leftsum = 0;
        int rightsum = 0;
        for(int i = 0; i < nums.length; i++){
            rightsum = nums[i] + rightsum;
        }
        for(int i = 0; i < nums.length; i++){
            rightsum = rightsum - nums[i];
            if(leftsum == rightsum){
                return i;
            }
            leftsum = nums[i] + leftsum;
        }
        return -1;
    }
}