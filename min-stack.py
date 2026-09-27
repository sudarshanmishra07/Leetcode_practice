class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack=[]                   #created another stack for min value

    def push(self, val: int) -> None:      #defined push function to push value in stack
        self.stack.append(val)
        if not self.minstack:
            self.minstack.append(val)
        else:
            self.minstack.append(min(val,self.minstack[-1]))

    def pop(self) -> None:                 ##defined pop function to pop value from stack
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:                  #defined top function to get top value of stack
        return self.stack[-1]

    def getMin(self) -> int:               #defined getMin function to get minimum value from stack
        return self.minstack[-1]
s=MinStack()                    #created object to check code
s.push(4)
s.push(3)
s.push(9)
s.push(2)

print(s.top())
print(s.getMin())
s.pop()
print(s.top())
print(s.getMin())