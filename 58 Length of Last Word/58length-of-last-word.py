class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        for i in s[::-1]:
            if(i.isspace() and length is not 0):
                return length
            if(not i.isspace()):
                length += 1
        return length