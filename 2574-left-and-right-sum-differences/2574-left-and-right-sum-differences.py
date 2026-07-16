class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = 0
        right = sum(nums)
        l = []
        for i in nums:
            left += i
            l.append(abs(left-right))
            right -=i
        return l

    