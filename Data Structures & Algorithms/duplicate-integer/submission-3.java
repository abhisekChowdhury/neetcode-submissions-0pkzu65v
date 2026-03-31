class Solution {
    public boolean hasDuplicate(int[] nums) {
        // Hashset solution in Java with enhanced for loop

        HashSet<Integer> numsHash = new HashSet<Integer>();
        for (int num : nums) {
            if (numsHash.contains(num)) {
                return true;
            } else {
                numsHash.add(num);
            }
        } return false;
    }
}