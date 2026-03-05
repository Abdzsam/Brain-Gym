class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for i in range(len(tokens)):
            if tokens[i][-1].isdigit():
                print(tokens[i][-1])
                stk.append(int(tokens[i]))
            else:
                if len(stk) > 1:
                    b = stk.pop()
                    a = stk.pop()
                    
                    if tokens[i] == "+":
                        stk.append(int(a + b))
                    elif tokens[i] == "-":
                        stk.append(int(a - b))
                    elif tokens[i] == "*":
                        stk.append(int(a * b))
                    else:
                        stk.append(int(a / b))

        return int(stk.pop())
                

        