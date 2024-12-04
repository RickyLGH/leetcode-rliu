class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequentnums = []
        frequency = defaultdict(int)
        for n in nums:
            frequency[n] += 1

        sortedlist = sorted(frequency.items() , key=lambda tup: tup[1], reverse=True)
        for i in range(k):
            frequentnums.append(sortedlist[i][0])
        return frequentnums
        