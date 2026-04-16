class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        right_prod = [1]
        left_prod = [1]

        for i in range(1,len(nums)):
            right_prod.append(right_prod[i-1]*nums[i-1])
        
        nums = nums[::-1]
        
        for i in range(1,len(nums)):

            left_prod.append(left_prod[i-1]*nums[i-1])

        com = []
        left_prod = left_prod[::-1]

        print(left_prod)
        print(right_prod)

        for i in range(0,len(left_prod)):
            com.append(left_prod[i]*right_prod[i])

        return com

        



        



        