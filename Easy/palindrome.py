# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         stack = []
#         valid_chars = "abcdefghijklmnopqrstuvwxyz0123456789"
#         hashmap = {char: True for char in valid_chars}
        
#         s = s.lower()
#         for i in s:
#             if i in hashmap:
#                 stack.append(i)

#         return stack == stack[::-1]

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_list = []
        for i in s:
            if i.isalnum():
                i = i.lower()
                new_list.append(i) 
        right = len(new_list)-1
        left = 0
        while left < right:
            if new_list[left] != new_list[right]:
                return False
            left +=1
            right -=1
        return True


            


