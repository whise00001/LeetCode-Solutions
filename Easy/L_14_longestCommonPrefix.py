'''
不清楚如何獲得陣列字串裡的第一個字元
一開始的想法是從第一個字串的第一個字元往後比，如果有不一樣就回傳之前的字元
'''


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = strs[0]
        pref_len = len(pref)

        for i in strs[1:]:
            while pref != i[0:pref_len]:
                pref_len -= 1
                if pref_len == 0:
                    return ""
                pref = pref[0:pref_len]
        
        return pref
