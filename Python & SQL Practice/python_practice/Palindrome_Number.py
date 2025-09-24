class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        
        1. if x < 0 - false (negative)
        2. if x > 0 - need to check true or false
        so first change x - int to y =  str(x)
        if len(y) = odd (%2 = 1)
        check first to (//2) from back too
        ex) len(y) = 5 then // 2 = 2 so first two / last two is same or not 
        if len(y) = even(%2 = 0)
        same check (//2)
        """

        if x < 0:
            return False
        elif x > 0:
            y = str(x)
            rev_y = y[::-1]
            if y[0:(len(y)//2)] == rev_y[0:len(y)//2]:
                return True
            else:
                return False
        else:
            return True