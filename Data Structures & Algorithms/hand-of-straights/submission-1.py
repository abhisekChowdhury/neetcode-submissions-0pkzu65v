class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)

        for num in sorted(count):
            while count[num] > 0:
                for i in range(groupSize):
                    if count[num+i]<=0:
                        return False
                    count[num + i] -= 1
        
        return True