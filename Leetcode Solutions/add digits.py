def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        add = 0
        flag = True
        while flag==True:
            for i in str(num):            
                add +=int(i)
            print(add)
            if add <10:
                return add
            else:
                num = add
                add =0