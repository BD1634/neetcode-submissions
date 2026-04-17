class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l = 0
        r = 0

        if len(s1) > len(s2):
            return False

        else:
            while l < len(s2) - len(s1) + 1:

                
                r = l + len(s1) - 1

                print(l,r)

                print(s2[l:r+1])

                if sorted(s1) == sorted(s2[l:r+1]):
                    return True
                else :
                    l = l + 1
        return False


        