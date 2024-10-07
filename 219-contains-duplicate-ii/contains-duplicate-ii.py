class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        x ={}

        for i , num in enumerate(nums):
            if num in x :
                if i - x[num] <= k:
                    return True
            x[num]=i

        return False
        