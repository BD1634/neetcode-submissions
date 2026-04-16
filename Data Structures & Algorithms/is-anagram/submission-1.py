class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        map1 = {}
        map2 = {}

        if len(s)!= len(t):
            return False

        else:
            for i in range(0,len(s)):
                if s[i] in map1:
                    map1[s[i]] += 1
                else:
                    map1[s[i]] = 1
                
                if t[i] in map2:
                    map2[t[i]] += 1
                else:
                    map2[t[i]] = 1
        
        print(map1)
        print(map2)
        
        for i in map1 :
            if i in map2:
                if map2[i] != map1[i]:
                    return False 
            else:
                return False

        return True
        