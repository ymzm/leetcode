class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k%length
        
        tmp = []
        
        for i in range(k):
            tmp.append(nums[length-k+i])
            
        for i in range(length - k):
            nums[length-1-i] = nums[length-1-i-k]
            
        for i in range(k):
            nums[i] = tmp[i]