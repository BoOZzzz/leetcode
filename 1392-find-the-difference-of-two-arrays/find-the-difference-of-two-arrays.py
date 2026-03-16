class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        array1 = list(set(nums1))
        array2 = list(set(nums2))
        num_map = defaultdict(int)
        #hashmap, + for array1, - for array2
        for i in range(len(array1)):
            num_map[array1[i]] += 1
        for i in range(len(array2)):
            num_map[array2[i]] -= 1
        ans1, ans2 = [], []
        for k, v in num_map.items():
            if v == 1:
                ans1.append(k)
            if v == -1:
                ans2.append(k)
        return [ans1,ans2]
        