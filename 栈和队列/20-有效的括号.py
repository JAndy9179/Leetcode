class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                temp = stack.pop()
                if c == ']' and temp != '[':
                    return False
                elif c == '}' and temp != '{':
                    return False
                elif c == ')' and temp != '(':
                    return False
        
        return True if len(stack) == 0 else False