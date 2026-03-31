class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> numHash = new HashMap<Integer, Integer>();
        
        for (int i = 0; i < nums.length; i++) {
            numHash.put(nums[i], i);
        }

        for (int i = 0; i < nums.length; i++) {
            if (numHash.get(target-nums[i]) != null){
                if (i != numHash.get(target-nums[i])){
                    int[] answer = {i, numHash.get(target-nums[i])};
                    return answer;
                }
            }
        }

        int[] zero = {0,0};
        return zero;
    }
}