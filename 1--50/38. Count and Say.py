"""The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence."""


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        def say_next(x):
            x_list = list(x)
            if x == '1':
                return '11'
            y = x_list[0]
            say = ''
            m = 1
            last = 0
            for z in x_list[1:]:
                last += 1
                if z == y:
                    m += 1
                else:
                    say = say + str(m) + y
                    y = z
                    m = 1
                if last == len(x_list) - 1:
                    say = say + str(m) + y
            return say

        say = '1'
        i = 1
        while i < n:
            i += 1
            say = say_next(say)
        return say

