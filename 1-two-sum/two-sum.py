class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hmap = {}
        for i in range(len(nums)):
            key = target - nums[i]
            if key in hmap:
                return [hmap[key], i]
            hmap[nums[i]] = i

