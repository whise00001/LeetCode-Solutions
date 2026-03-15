class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def get_next_index(s,end):
            backspace = 0
            while end >= 0 :
                if s[end] == '#':
                    backspace += 1
                elif backspace > 0:
                    backspace -=1
                else:
                    break
                end -= 1
            return end


        ps = len(s) - 1
        pt = len(t) - 1

        while ps >= 0 or pt >= 0:
            ps = get_next_index(s,ps)
            pt = get_next_index(t,pt)

            
            if ps < 0 and pt < 0:
                return True
            elif ps < 0 or pt < 0 :
                return False
            elif s[ps] != t[pt]:
                return False    
            
            ps -= 1
            pt -=1

        return True
