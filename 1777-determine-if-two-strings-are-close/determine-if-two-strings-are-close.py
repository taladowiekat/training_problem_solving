class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        
        if set(word1) != set(word2):
            return False

        f_w1={}
        f_w2={}
        for char in word1:
            if char in f_w1:
                f_w1[char]+=1
            else:
                f_w1[char] = 1

        
        for char in word2:
            if char in f_w2:
                f_w2[char]+=1
            else:
                f_w2[char] = 1

        if sorted(f_w1.values()) != sorted(f_w2.values()):
            return False

        return True
        
