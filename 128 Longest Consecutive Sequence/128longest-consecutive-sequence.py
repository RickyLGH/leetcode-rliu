class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        maxsequence =  0
        for i in hashset:
            if i - 1 not in hashset:
                length = 1
                while(i + length in hashset):
                    length += 1
                maxsequence = max(maxsequence, length)
        return maxsequence