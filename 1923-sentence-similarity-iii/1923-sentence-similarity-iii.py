class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split()
        words2 = sentence2.split()
        
        len1, len2 = len(words1), len(words2)
        i = 0
        while i < len1 and i < len2 and words1[i] == words2[i]:
            i += 1            
        j = 0
        while j < (len1 - i) and j < (len2 - i) and words1[len1 - 1 - j] == words2[len2 - 1 - j]:
            j += 1
            
        return i + j >= len1 or i + j >= len2
