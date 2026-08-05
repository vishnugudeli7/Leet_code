class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
    #     left = 0
    #     right = len(nums)-1
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        else:
            return len(nums)