class Solution:
    def isValid(self, s: str) -> bool:
        d = {')':'(',']':'[','}':'{'}
        stack = []
        for i in s:
            if i in d:
                element = stack.pop() if stack else '#'
                if d[i] != element:
                    return False
            else:
                stack.append(i)
        return not(stack)