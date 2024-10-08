class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        s =set(nums) # because looking for a number in a set vary fast
        long_sequence =0
        num = 0
        sequence = 0
        for i in s :
            if i-1 not in s :
                num = i
                sequence=1
            while num +1 in s:
                num+=1
                sequence+=1

            long_sequence = max(long_sequence ,sequence )
        return long_sequence