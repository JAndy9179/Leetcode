class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    temp = stack.pop()
                    if c == ')' and temp == '(':
                        continue
                    elif c == ']' and temp == '[':
                        continue
                    elif c == '}' and temp == '{':
                        continue
                    else:
                        return False
        
        return True if not stack else False