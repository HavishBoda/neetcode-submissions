class Solution:
    def isValid(self, s: str) -> bool:
        mappings = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        stack = []
        for char in s:
            if char not in mappings:
                stack.append(char)
            else:
                if not stack:
                    return False
                if mappings[char] != stack[-1]:
                    return False
                stack.pop()
        
        return len(stack) == 0