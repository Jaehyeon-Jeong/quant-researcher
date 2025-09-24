class Solution:
    def isPalindrome(self, x: int):
        str_x = str(x)
        rev_x = str_x[::-1]

        if str_x == rev_x:
            return True
        else:
            return False
