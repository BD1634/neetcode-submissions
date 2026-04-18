# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        l = 1
        h = n

        while l<=h:

            if guess((l+h)//2) == 0:
                return (l+h)//2
            
            elif guess((l+h)//2) == -1:
                h = (l+h)//2 - 1
            else:
                l = (l+h)//2 + 1

        



        