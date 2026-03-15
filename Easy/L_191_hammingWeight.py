class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            if n%2 > 0:
                count += 1
            n = n // 2

        for i in ans:
            if i == 1:
                count += 1 
        
        return count
