#S and T are given as strings

Solution #2

#Language used--Python3
def backspaceCompare(self, S: str, T: str) -> bool:
    stack1=[]
    stack2=[]

    for i in S:
        if i=='#':
            if not len(stack1)==0:
                stack1.pop()
        else:
            stack1.append(i)

    for i in T:
        if i=='#':
            if not len(stack2)==0:
                stack2.pop()
        else:
            stack2.append(i)

    return stack1==stack2
