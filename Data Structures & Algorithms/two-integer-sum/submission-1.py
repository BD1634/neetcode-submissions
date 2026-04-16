class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1 = {}

        for i , n in enumerate(nums):
            map1[n] = i
        
        for i , n in enumerate(nums):


            diff = target - n

            if diff in map1 and map1[diff] !=i:
                return [i,map1[diff]]
        return []



        
        



        