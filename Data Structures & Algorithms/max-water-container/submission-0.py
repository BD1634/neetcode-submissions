class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0
        r = len(heights) - 1

        max_prod = 0

        while l < r :

            max_prod = max(max_prod , (min(heights[l],heights[r])*(r-l)))

            if heights[l] < heights[r] :
                l = l+1
            else:
                r = r - 1
        
        return max_prod
        