class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num = 0
        for i in range(len(nums)):
            num = nums[i] ^ num
        return num