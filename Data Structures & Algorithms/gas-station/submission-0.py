class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0 #total gas
        current = 0 #current tank
        start = 0 #start index

        for i in range(len(gas)):
            gain = gas[i] - cost[i]

            total += gain
            current += gain

            #if we run out of gas
            if current < 0:
                start = i+1
                current = 0 #reset tank
        
        return start if total >= 0 else -1