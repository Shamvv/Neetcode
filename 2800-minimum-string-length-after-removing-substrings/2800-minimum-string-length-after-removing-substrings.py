class Solution:
    def minLength(self, s: str) -> int:
        while "AB" in s or "CD" in s:
            for i in range(len(s)):
                if s[i:i+2] == "AB" or s[i:i+2] == "CD":
                    #print(s[i:i+2])
                    s = s[0:i] + s[i+2:]
                    #print(s[0:i], s[i+2:], s)
            #print(s)
        return len(s)
        