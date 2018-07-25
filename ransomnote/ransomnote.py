class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dict = {}
        
        for i in magazine:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
                
        for i in ransomNote:
            if i in dict:
                if dict[i] == 0:
                    return False
                dict[i] -= 1
            else:
                return False
            
        return True