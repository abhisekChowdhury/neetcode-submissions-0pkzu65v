class Solution {
    public boolean hasDuplicate(int[] nums) {
        // Hashset solution in Java with enhanced for loop and Set

        Set<Integer> numsHash = new HashSet<Integer>();
        for (int num : nums) {
            if (!numsHash.add(num)){
                return true;
            }
        } return false;
    }
}