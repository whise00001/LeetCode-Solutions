class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap = {}

        for i in s:
            hashmap[i] = hashmap.get(i,0) + 1
        
        for i in t:
            if i not in hashmap or hashmap[i] == 0 :
                return False
            else:
                hashmap[i] -= 1
        return True
