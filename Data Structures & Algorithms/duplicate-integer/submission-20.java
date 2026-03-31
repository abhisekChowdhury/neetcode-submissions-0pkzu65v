class Solution {
    public boolean hasDuplicate(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            int temp = nums[i];
            for (int j = 0; j < nums.length; j++) {
                if (i==j) {
                     break;
                    } else {
                        if (temp == nums[j]) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
}