class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = {}

        while strs:
            word = strs.pop(0)  # take first element
            group = [word]
            
            remaining = []
            
            for other in strs:
                if sorted(word) == sorted(other):
                    group.append(other)
                else:
                    remaining.append(other)
            
            anagrams[word] = group
            strs = remaining  # update list safely

        anagrams_new = []

        for i in anagrams:
            anagrams_new.append(anagrams[i])

        return anagrams_new
                


            
                    


            


        