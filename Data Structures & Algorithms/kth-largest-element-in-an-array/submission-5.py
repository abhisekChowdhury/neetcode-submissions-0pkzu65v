class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #naive approach:
        # sort the array
        # return the kth value from the back.
        # Time - O(nlogn) Space -O(1)
        #[2,3,1,5,4]
        #[1,2,3,4,5] and k = 2
        # 5-2 = 3, so return the len(nums)-kth value


        nums.sort()
        return nums[(len(nums)-k)]