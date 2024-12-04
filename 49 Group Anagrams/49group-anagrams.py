class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for string in strs:
            sortedstr = str(sorted(string))
            anagrams[sortedstr].append(string)
        return list(anagrams.values())