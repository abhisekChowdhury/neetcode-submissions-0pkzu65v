class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        fruit_type_count = defaultdict(int)
        max_count = 0
        num_of_baskets = 2

        for right in range(len(fruits)):
            #expand
            fruit_type_count[fruits[right]]+=1

            #shrink
            while len(fruit_type_count) > num_of_baskets:
                fruit_type_count[fruits[left]]-=1
                if fruit_type_count[fruits[left]]==0:
                    del fruit_type_count[fruits[left]]
                left+=1

            max_count = max(max_count, right-left+1)
        
        return max_count