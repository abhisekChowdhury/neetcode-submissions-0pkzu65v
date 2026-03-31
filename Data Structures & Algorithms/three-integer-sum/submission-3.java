class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);

        int left = 0;
        int right = 0;
        List<List<Integer>> answer = new ArrayList<>();

        for (int i = 0; i < nums.length-1; i++) {
            left = i+1;
            right = nums.length-1;

            if (i > 0) {
                if (nums[i] == nums[i-1]){
                    continue;
                }
            }

            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                
                if (sum == 0) {
                    answer.add(new ArrayList<>(List.of(nums[i], nums[left], nums[right])));
                    left++;
                    right--;

                    while (left < right && nums[left] == nums[left-1]){
                        left++;
                    }

                    if(right<nums.length-1){
                        while (left < right && nums[right] == nums[right+1]){
                            right--;
                        }
                    }
                }
                else if (sum < 0) {
                    left ++;
                } else {
                    right--;
                }
                
            }
        }

        return answer;
    }
}
