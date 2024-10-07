class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        v = 0

        for i in range(len(nums)):
            if i > v :
                return False
            v=max(v,i+nums[i])

            if v >= len(nums)-1:
                return True
            
        
        return False