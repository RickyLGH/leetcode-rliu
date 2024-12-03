class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = defaultdict(int)
        for i in range(len(nums)): 
            targetnum = target - nums[i]
            if targetnum in hashmap.keys():
                return [i, hashmap[targetnum]]
            hashmap[nums[i]] = i
