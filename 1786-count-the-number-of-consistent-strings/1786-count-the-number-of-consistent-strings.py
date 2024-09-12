class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        l = []
        check = set(allowed)
        count = 0
        for i in words:
            word = set(list(i))
            for i in word:               
                if i not in check:
                    count += 1
                    break
        return len(words) - count