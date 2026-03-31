class Solution {
    public boolean hasDuplicate(int[] nums) {
        //     for (int i = 0; i < nums.length; i++) {
        //         for (int k = 0; k < nums.length; k++) {
        //             if (i!=k){
        //                 if (nums[i] == nums[k]) {
        //                     return true;
        //                 }
        //             }
        //         }
        // }
        // return false;

        // Hashset solution in Java

        HashSet<Integer> numsHash = new HashSet<Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (numsHash.contains(nums[i])) {
                return true;
            } else {
                numsHash.add(nums[i]);
            }
        } return false;
    }
}