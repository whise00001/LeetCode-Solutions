class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = {}
        for i in magazine:
            hashmap[i] = hashmap.get(i,0) + 1

        for i in ransomNote:
            if i in hashmap and hashmap[i] != 0:
                hashmap[i] -= 1
            else:
                return False
        return True
