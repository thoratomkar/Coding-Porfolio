def shortestCompletingWord(self, licensePlate, words):
        lpcc = {} #license plate char count
        for l in licensePlate:
            if l.isalpha():
                l = l.lower()
                if l in lpcc:
                    lpcc[l] += 1
                else:
                    lpcc[l] = 1

        words.sort(key = len) #sort words by length
        for word in words:
            copy = dict(lpcc)
            for letter in word:
                if letter in copy:
                    if copy[letter] > 1:
                        copy[letter] -= 1
                    else:
                        del copy[letter]
                        if len(copy) == 0:
                            return word