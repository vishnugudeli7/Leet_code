class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # for i in range(len(nums)+1):
        n = len(nums)
        actual_sum = n * (n+1)//2
        list_sum = sum(nums)
        return (actual_sum - list_sum)


