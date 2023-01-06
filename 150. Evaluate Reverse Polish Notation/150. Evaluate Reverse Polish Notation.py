#https://leetcode.com/problems/evaluate-reverse-polish-notation/description
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators={'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
        stack=[]
        for i in range(len(tokens)):
            if tokens[i] in operators:
                temp=operators[tokens[i]](int(stack[-2]), int(stack[-1]))
                stack.pop()
                stack.pop()
                stack.append(temp)
            else:
                stack.append(tokens[i])
        return int(stack[-1]) 
                
                
