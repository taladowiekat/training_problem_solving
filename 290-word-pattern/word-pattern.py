class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split(' ')
 
        if len(pattern) != len(words) :
            return False

        dic1 = {}
        dic2 = {}

        for i , j in zip(pattern,words):
            if i in dic1 :
                if dic1[i]!= j:
                    return False
            else:
                dic1[i]=j
            
            if j in dic2:
                if dic2[j]!=i:
                    return False

            else:
                dic2[j]=i
        return True