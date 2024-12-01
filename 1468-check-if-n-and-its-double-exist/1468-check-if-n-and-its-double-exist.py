class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if arr.count(0) >= 2:
            return True
        for i in arr:
            if 2 * i in arr:
                a, b = arr.index(i), arr.index(2*i)
                if a != b:
                    return True
        return False
        