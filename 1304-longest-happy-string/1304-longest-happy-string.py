class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result = []
        
        while a > 0 or b > 0 or c > 0:
            options = [('a', a), ('b', b), ('c', c)]
            options.sort(key=lambda x: -x[1])
            
            for char, count in options:
                if count > 0 and (len(result) < 2 or not (result[-1] == char and result[-2] == char)):
                    result.append(char)
                    if char == 'a':
                        a -= 1
                    elif char == 'b':
                        b -= 1
                    else:
                        c -= 1
                    break
            else:
                break

        return ''.join(result)