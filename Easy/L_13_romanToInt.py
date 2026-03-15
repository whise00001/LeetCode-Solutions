class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        nums = 0

        for a,b in zip(s,s[1:]):
            if hashmap[a] >= hashmap[b]:
                nums += hashmap[a]
            else:
                nums -= hashmap[a]
        nums += hashmap[s[-1]]

        return nums

            
            