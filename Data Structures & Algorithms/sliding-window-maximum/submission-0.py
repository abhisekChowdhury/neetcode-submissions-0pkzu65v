class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        if k > len(nums):
            return []
        
        index_deque = deque()
        window_maxes = []

        for current_index in range(len(nums)):

            if index_deque and index_deque[0] <= current_index - k:
                index_deque.popleft()
            
            while index_deque and nums[index_deque[-1]] <= nums[current_index]:
                index_deque.pop()
            
            index_deque.append(current_index)

            if current_index >= k - 1:
                window_maxes.append(nums[index_deque[0]])
        
        return window_maxes