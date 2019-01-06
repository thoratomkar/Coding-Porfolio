class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l=len(haystack)
        
        if needle=="":
            return 0
        
        elif needle in haystack:
            return haystack.find(needle)
        
        else:
            return -1
            