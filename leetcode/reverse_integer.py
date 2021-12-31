# https://leetcode.com/problems/reverse-integer/

class Solution(object):
    def reverse(self, x: int) -> int:
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            x = str(x)[1:][::-1]

            while x[0] == '0':
                x = x[1:]

            x = 0-int(x)

            if x < -2**31:
                return 0

            return x

        else:
            if x <10:
                return x

            x = str(x)[::-1]

            while x[0] == '0':
                x = x[1:]

            x = int(x)

            if x > (2**31)-1:
                return 0

            return x