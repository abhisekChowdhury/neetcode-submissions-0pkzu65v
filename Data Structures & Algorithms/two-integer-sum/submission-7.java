class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hashNums = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int temp = target-nums[i];
            if (hashNums.containsKey(temp)) {
                return new int[] {hashNums.get(temp),i};
            }

            // put the value: nums[i] and key: i in hashNums only 
            // when the above if statement is not satisfied.
            hashNums.put(nums[i],i);
        }
        return new int[] {0};
    }
}
