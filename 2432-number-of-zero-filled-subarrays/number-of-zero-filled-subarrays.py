class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # subarrays = defaultdict(int)
        # arr_size = 0
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         arr_size += 1
        #     if nums[i] != 0 and arr_size != 0:
        #         subarrays[arr_size] += 1
        #         arr_size = 0
        # if arr_size != 0:
        #     subarrays[arr_size] += 1
        # sum_arrs = 0
        # for i, v in subarrays.items():
        #     sum_arrs += v*((i)*(i+1))/2
        # return sum_arrs

        ans = 0
        cur = 0

        for num in nums:
            if num == 0:
                cur += 1
            else:
                cur = 0
            
            ans += cur

        return ans