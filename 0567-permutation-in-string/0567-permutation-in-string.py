class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        count1 = [0] * 26
        count2 = [0] * 26
        
        if n1 > n2:
            return False
        
        for i in range(n1):
            count1[ord(s1[i]) - 97] += 1
            count2[ord(s2[i]) - 97] += 1
        
        if count1 == count2:
            return True

        for i in range(n1, n2):
            count2[ord(s2[i]) - 97] += 1
            count2[ord(s2[i - n1]) - 97] -= 1
            if count1 == count2:
                return True
        return False
        
        """
        s11 = [0] * 26
        s22 = [0] * 26

        for i in s1:
            s11[ord(i) - 97] += 1            

        for j in s2:
            s22[ord(j) - 97] += 1

        s1_ = ''.join(str(num) for num in s11)
        s2_ = ''.join(str(num) for num in s22)

        print(s11, s22)
        
        f = 0
        for i in range(26):
            if s11[i] == 1:
                if s11[i] == s22[i]:
                    continue
                else:
                    f = 1
        
        return f == 0
        """