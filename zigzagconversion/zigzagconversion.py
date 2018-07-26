class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        
        step = 0
        index = 0
        L = [""]*numRows
        for i in s:
            L[index] += i
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step
        
        return "".join(L)