# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        mi = 1
        ma = n
        a = (mi + ma) // 2
        while mi < ma:
            if isBadVersion(a):
                ma = a
            else:
                mi = a + 1
            a = (mi + ma) // 2
        return a
        
        
