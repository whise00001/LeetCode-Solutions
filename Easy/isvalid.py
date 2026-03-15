class Solution:
    def isValid(self, s: str) -> bool:
        hashmap={")":"(","}":"{","]":"["}
        stack=[]
        for i in s:
            if i in hashmap.values():
                stack.append(i)
            elif i in hashmap.keys():
                if not stack or hashmap[i]!=stack.pop():
                    return False
        return not stack