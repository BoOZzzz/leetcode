class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        

        used = [0] * len(baskets)
        placed = 0
        for fruit in fruits:
            for b in range(len(baskets)):
                if fruit <= baskets[b] and used[b] == 0:
                    used[b] += 1
                    placed += 1
                    break
        

        return len(fruits) - placed