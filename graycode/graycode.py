class Solution(object):
    def grayCode(self, n):
        def gc(n):
            if n == 1:
                return [0,1]
            elif n == 0:
                return [0]
            else:
                ret2 = []
                ret1 = gc(n-1)
                size = len(ret1)
                for i in range(size):
                    ret2.append(ret1[size-1-i] | (1<<(n-1)))
                return ret1+ret2
        
        ret = gc(n)
        return ret

