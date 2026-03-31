class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> numsHash = new HashSet<Integer>();
        for (int num : nums) {
            if (numsHash.contains(num)){
                return true;
            } else {
                numsHash.add(num);
            }
        }
        return false;
    }
}