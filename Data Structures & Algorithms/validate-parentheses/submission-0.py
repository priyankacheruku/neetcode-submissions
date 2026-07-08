class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {"{":"}","[":"]","(":")"}
        for i in s:
            if i  in d.keys():
                stack.append(i)
            else:
                if not stack:
                    return False
                if i ==d.get(stack[-1]):
                    stack.pop()
                else:
                    return False
        if len(stack):
            return False
        return True

        