class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        s = mean * (m + n)
        snow = sum(rolls)
        diff = s - snow

        if diff < n or diff > 6 * n:
            return []

        avg, remainder = divmod(diff, n)
        result = [avg + 1] * remainder + [avg] * (n - remainder)
        
        return result