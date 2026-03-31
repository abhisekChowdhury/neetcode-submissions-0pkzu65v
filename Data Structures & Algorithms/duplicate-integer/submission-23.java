class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> numsHash = new HashSet<Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (numsHash.contains(nums[i])){
                return true;
            } else {
                numsHash.add(nums[i]);
            }
        }
        return false;
    }
}