class Ram:
    def __init__(self):
        self.values=[]
    def push(self,x):
        self.values.append(x)
    def pop(self):
        return self.values.pop(0)      



s=Ram()
s.push(88)
s.push(86)
s.push(3)
s.pop()
print(s.values)
    