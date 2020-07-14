class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        S = [x for x in S]
        T = [x for x in T]
        counter1=0
        while(counter1 < len(S)):
            elem = S[counter1]
            if elem == '#':
                counter2 = counter1-1
                while(counter2 >= 0):
                    if S[counter2] != '#':
                        S[counter2] = '#'
                        break
                    counter2 -=1
            counter1 += 1
        counter1 = 0
        while(counter1 < len(T)):
            elem = T[counter1]
            if elem == '#':
                counter2 = counter1-1
                while(counter2 >= 0):
                    if T[counter2] != '#':
                        T[counter2] = '#'
                        break
                    counter2 -= 1 
            counter1 += 1
        new_S = [x for x in S if x!='#']
        new_T = [x for x in T if x!='#']
        
        if "".join(new_S) =="".join(new_T):
            return True
        return False
