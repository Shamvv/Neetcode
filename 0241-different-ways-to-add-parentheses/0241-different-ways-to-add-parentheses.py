class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]
        res = []
        for i, char in enumerate(expression):
            if char in "+-*":
                left = expression[:i]
                right = expression[i+1:]
                left_res = self.diffWaysToCompute(left)
                right_res = self.diffWaysToCompute(right)
                for l in left_res:
                    for r in right_res:
                        if char == "+":
                            res.append(l + r)
                        elif char == "-":
                            res.append(l - r)
                        elif char == "*":
                            res.append(l * r)
        return res

