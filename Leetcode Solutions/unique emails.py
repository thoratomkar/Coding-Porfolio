def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        
        email = []
        index1 = 0
        index2 = 0
        for i in range(len(emails)):
            
            x = list(emails[i])
            
            if '+' in x:
                index1 = x.index('+')
                index2 = x.index('@')
                
                for i in range(index1,index2):
                    x[i] = ""
                
            index2 = x.index('@')    
            for i in range(0,index2):
                if x[i] == '.':
                    x[i] = ""
            temp = "".join(x)
            
            email.append(temp)
        
        return len(set(email))
        """   
        
        email_list = []
        for e in emails:
            e0 = e.split('@')
            e1 = e0[0].split('+')
            e2 = e1[0].replace('.','')
            email = e2 + '@' + e0[1]
    
            email_list.append(email)
            #cnt = set(email_list)
        
        return (len(set(email_list))); 