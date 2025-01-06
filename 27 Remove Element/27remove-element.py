class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        occ = 0
        for i in nums:
            if i == val:
                occ += 1
        for i in range(occ):
            nums.remove(val)
        return len(nums)