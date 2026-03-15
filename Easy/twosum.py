# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 ans=(nums[i]+nums[j])
#                 if(target==ans):
#                     return [i,j]

class Solution:
    def twoSum(self,nums:List[int],target:int):
        hashmap={}
        for i in range(len(nums)):
            hashmap[nums[i]]=i
        for i in range(len(nums)):
            ans=target-nums[i]
            if ans in hashmap and hashmap[ans] !=i:
                return [i,hashmap[nums[i]] ]