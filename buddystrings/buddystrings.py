class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        length = len(A)
        if length != len(B):
            return False
        
        diff_cnt = 0
        diff = [0,0]
        i = 0
        while i < length:
            if A[i] != B[i]:
                if diff_cnt == 2:
                    return False
                diff[diff_cnt] = i
                diff_cnt+=1
            i+=1
            
        if diff_cnt == 0:
            return len(A) != len(set(A))
        if diff_cnt == 1:
            return False
        
        return A[diff[0]] == B[diff[1]] and A[diff[1]] == B[diff[0]]