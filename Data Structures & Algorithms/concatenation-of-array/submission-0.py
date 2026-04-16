class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        num = nums.copy()
        for i in num:
            nums.append(i)
        return nums
        