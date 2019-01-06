class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        
        """
        Roman_dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        sum = Roman_dic[s[len(s)-1]]    # pick the last element
        i = len(s) -2
        while i>= 0:
            if Roman_dic[s[i]] < Roman_dic[s[i+1]]:
                sum -= Roman_dic[s[i]]
            else:
                sum += Roman_dic[s[i]]
            i -= 1
        return sum
            
        