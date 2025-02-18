class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        li = set()
        for num in nums:
            if num in li:
                return True
            li.add(num)
        return False