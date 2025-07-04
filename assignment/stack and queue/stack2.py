class stack:
    
    def __init__(self,size):
        self.sp=-1
        self.size=size
        self.stack_list=[]
    def overflow(self):
        return self.sp==self.size-1
    def push(self,data):
        if self.overflow():
            print("stack overflow")
        else:
            self.stack_list.insert(0,data)
            self.sp=self.sp+1
            print("data added to stack")
        
    def underflow(self):
        return self.sp==-1
    def pop(self):
        if self.underflow():
            print("stack underflow")
        else:
            self.stack_list.pop()
            self.sp=self.sp-1
            print("data removed from stack")
    def traverse(self):
        print(self.stack_list)
n=int(input("enter the size of stack"))
s1=stack(n)
while True:
    print('''enter 1 for push ,
enter 2 for pop
enter 3 for traverse
enter 4 for exit''')
    operation=int(input())
    if operation==1:
        value =int(input("enter the psuh value"))
        s1.push(value)
    elif operation==2:
        s1.pop()
    elif operation==3:
        s1.traverse()
    elif operation==4:
        print("exiting program")
        break
    else :
        print("invalid input")
    
    
