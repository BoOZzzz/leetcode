class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        
        fruit_baskets = defaultdict(int)
        start = 0
        current_max = 0

        for end in range(len(fruits)):
            fruit_baskets[fruits[end]] += 1

            while len(fruit_baskets) > 2:
                fruit_baskets[fruits[start]] -= 1
                if fruit_baskets[fruits[start]] == 0:
                    del fruit_baskets[fruits[start]]
                start += 1
            
            current_max = max(current_max, end - start + 1)

        return current_max
            