class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        res = set()                                           
        for i in range(len(text)):                           
            for l in range(1,len(text)-i):                
                if text[i] == text[i+l]:                      
                    k = 1                                    
                    while i+(k+1)*l <= len(text):
                        if text[i:i+k*l] == text[i+k*l:i+(k+1)*l]:
                            res.add(text[i:i+(k+1)*l])
                            k *= 2                            
                        else:
                            break
        return len(res)
