def commonChars(self, A: List[str]) -> List[str]:
        
        answer = None
        
        for a in A:
            work = {}
            
            for c in a:
                if c in work:
                    work[c] += 1
                else:
                    work[c] = 1
            
            if answer != None:
                
                keys = list(answer.keys())                
                for k in keys:
                    
                    if k in work:
                        answer[k] = min(work[k],answer[k])
                    else:
                        del answer[k]
            else:
                answer = work
            
        result = []
        #print (answer.keys())
        for key in answer.keys():
            #print(key)
            count = answer[key]
            for _ in range(count):
                result.append(key)

        return result
                    
                    
            