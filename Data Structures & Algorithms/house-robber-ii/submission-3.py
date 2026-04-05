class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        nums1 = nums[:-1]
        dp = [0] * len(nums1)

        if len(nums1) == 1:
            ans1 = nums1[0]
        else:
            dp[0] = nums1[0]
            dp[1] = max(nums1[0], nums1[1])

            for i in range(2,len(nums1)):
                dp[i] = max(dp[i-1], nums1[i] + dp[i-2])
            
            ans1 = dp[-1]

        nums2 = nums[1:]
        dp = [0] * len(nums2)

        if len(nums2) == 1:
            ans2 = nums2[0]
        else:
            dp[0] = nums2[0]
            dp[1] = max(nums2[0], nums2[1])

            for i in range(2,len(nums2)):
                dp[i] = max(dp[i-1], nums2[i] + dp[i-2])
            
            ans2 = dp[-1]

        return max(ans1,ans2)