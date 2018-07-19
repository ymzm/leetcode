class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        
        range_tmp = n
        ret_list = []
        max_prime = 1
        max_prime_tmp = max_prime
        
        while range_tmp > max_prime*max_prime:
            max_prime_tmp = max_prime_tmp + 1;
            while (range_tmp % max_prime_tmp) == 0:
                range_tmp = range_tmp / max_prime_tmp
                ret_list.append(max_prime_tmp)
                max_prime = max_prime_tmp
        
        sum = 0
        for i in ret_list:
            sum += i
        
        if range_tmp > 1:
            sum += range_tmp
        return sum