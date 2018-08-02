class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        arr =  []
        flag = -1
        if num >= 0:
            flag  = 1
        num = num*flag
        while num/7 > 0:
            arr.append(num%7)
            num = num /7
        arr.append(num)
        ret = "" if flag == 1 else "-"
        for i in arr[::-1]:
            ret += str(i)
        return ret