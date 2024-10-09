class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_of_jumps = 0
        x = 0
        y = 0

        for i in range(len(nums)-1):
            y = max(y,i+nums[i])

            if i == x :
                num_of_jumps +=1
                x = y 

        return num_of_jumps