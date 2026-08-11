class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # return a result array of daily temperatures consisting of the number of days after the ith day before a warmer temperature appears

        # start with an array[0,0,0,0,0..n]
        # in case a warmer day does not appear for any one or more days, the value will remain 0.

        # naive approach:
        # set a result list of [0,0,0...]
        # loop through each day from the temperatures list.
            # loop through each day starting from day_index + 1 to len(temperatures)
                # if future day temperature is greater than current day_index temperature
                    # set the future_day_index - current_day_index to the result[current_day_index]
        # finally, return the result.

        # This is not optimal as Time complexity will be O(n^2) and Space will be O(n) for the size of the array

        # I can optimize this by introducing a stack which will keep a track of the days indexes that have not seen a warmer day yet. And every time I find a warmer day than the top of the stack, I will go ahead and resolve that. This will bring my time complexity down to O(n), which is much better than the approach before.

        # temperatures = [22,21,25,24,27]

        result = [0] * len(temperatures) #[0,1,0,0,0]
        unresolved_stack = [] #[]

        for curr_day_idx in range(len(temperatures)): #0
            #  [0,1,2,3]                  21                                   25
            while unresolved_stack and temperatures[unresolved_stack[-1]] < temperatures[curr_day_idx]:
                resolve_idx = unresolved_stack.pop() #1
                result[resolve_idx] = curr_day_idx - resolve_idx
            # [0,1]
            unresolved_stack.append(curr_day_idx)
        
        return result