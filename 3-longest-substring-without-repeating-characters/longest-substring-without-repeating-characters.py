class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        #sliding window, use a left and right pointer to simplify algorithm
        l, res = 0, 0 #pointer to subtract, solution var
        r = 0 #pointer to add
        window = set() # cheeck duplicate
        while r < len(s): #iterate through given list str
            while s[r] in window:   #iterate through window to remove dups
                window.remove(s[l]) #remove dups from window
                l+=1 #shorten window size
            window.add(s[r]) #add new element to window
            res = max(res, r-l+1) #update max window size
            r+=1 #increase window size

        return res