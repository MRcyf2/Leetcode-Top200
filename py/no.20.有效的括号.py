class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i=='(' or i=='{' or i=='[':
                stack.append(i)
            elif i==')':
                if stack==[] or stack.pop()!='(':
                    return False
            elif i=='}':
                if stack==[] or stack.pop()!='{':
                    return False
            elif i==']':
                if stack==[] or stack.pop()!='[':
                    return False
        if stack==[]:
            return True
        else:
            return False