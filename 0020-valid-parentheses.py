class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {"(":")", "[":"]", "{": "}"}
        stack = []
        for bracket in s:
            if bracket in bracket_map:
                stack.append(bracket)
            else:
                if stack != []:
                    op_bracket = stack.pop()
                else:
                    return False
                #if bracket is value of popped key bracket
                if bracket != bracket_map[op_bracket]:
                    return False
        return len(stack) == 0


if __name__ == "__main__":
    s = Solution()
    print(s.isValid("(["))