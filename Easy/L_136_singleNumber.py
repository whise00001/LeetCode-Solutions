'''
初步想法:
    想到hashmap紀錄每個數出現的次數
    Time complexity:O(n)
    Space complexity:O(n)
進階:
    可以使用XOR的特性兩兩消除
    Time complexity:O(n)
    Space complexity:O(1)
'''

# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         hashmap = {}
#         for i in nums:
#             hashmap[i] = hashmap.get(i,0) + 1

#         for i in hashmap:
#             if hashmap[i] == 1:
#                 return i          
   
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        for n in nums:
            res ^= n

        return res 