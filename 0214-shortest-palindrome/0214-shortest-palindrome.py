class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s: return s
        rev_s = s[::-1]
        concat = s + "#" + rev_s
        
        lps = [0] * len(concat)
        length = 0
        i = 1
        
        while i < len(concat):
            if concat[i] == concat[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        pal_len = lps[-1]
        to_add = rev_s[:len(s) - pal_len]
        return to_add + s