def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        res = []
        text = text.split()
        for i in range(len(text)-2):
            #print(text[i])
            if text[i] == first and text[i+1] == second:
                res.append(text[i+2])
        
        return res
    