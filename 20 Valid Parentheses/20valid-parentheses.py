class Solution:
    def isValid(self, s: str) -> bool:
        paren = []
        for string in s:
            if string == '(' or string == '{' or string == '[':
                paren.append(string)
            else:
                if len(paren) == 0:
                    return False
                first =  paren.pop()
                if string == ')':
                    if first != '(':
                        return False
                if string == '}':
                    if first != '{':
                        return False
                if string == ']':
                    if first != '[':
                        return False
        if len(paren) == 0:
            return True
        return False
