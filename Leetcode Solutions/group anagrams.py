def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict ={}
        for str in strs:
            sortedStr = "".join(sorted(str))
            if sortedStr in dict:
                dict[sortedStr].append(str)
            else:
                dict[sortedStr] =[str]

        
        return dict.values()