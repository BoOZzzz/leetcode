# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        #binary search

        lp = 1
        rp = n
        while lp < rp:
            mid = (lp+rp)//2
            
            if isBadVersion((lp+rp)//2) is False:
                lp = mid+1
            else:
                rp = mid

        return lp