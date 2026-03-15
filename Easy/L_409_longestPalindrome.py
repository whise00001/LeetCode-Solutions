class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap = {}
        long = 0
        for i in s :
            hashmap[i] = hashmap.get(i,0) + 1
            if hashmap[i] >= 2:
                hashmap[i] -= 2
                long += 2
        for i in hashmap.values() :
            if i > 0:
                return long + 1
        
        return long
            
        
        
            