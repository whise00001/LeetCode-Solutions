class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = majority = 0

        for i in nums:
            if majority == 0:
                res = i
            if res == i :
                majority +=1
            else:
                majority -=1
        return res
                

