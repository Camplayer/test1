class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        dic = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        
        result = 0
        num = len(s)
        if num == 0:
        	return 0
        pre = dic[s[0]]
        result += pre
        for i in range(1, num):
        	cur = dic[s[i]]
        	result += cur
        	if cur > pre:
        		result -= 2 * pre
        	pre = cur
        return result

ex = Solution()
s = "IX"
print ex.romanToInt(s)