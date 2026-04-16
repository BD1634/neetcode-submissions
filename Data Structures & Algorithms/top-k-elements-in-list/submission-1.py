class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hmap = {}

        for i in nums:
            if i in hmap:
                hmap[i] = hmap[i] + 1
            else:
                hmap[i] = 1
        
        hmap = sorted(hmap, key=hmap.get)



        return list(hmap)[-k:]
            




        
        


        
        