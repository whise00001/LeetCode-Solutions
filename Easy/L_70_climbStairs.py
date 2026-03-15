class Solution:
    def climbStairs(self, n: int) -> int:
        pre1 = 2
        pre2 = 3
        cur = 0
        if n < 4 :
            return n


        for i in range(3,n):
            cur = pre1 + pre2    
            pre1 = pre2
            pre2 = cur
        
        return cur
        