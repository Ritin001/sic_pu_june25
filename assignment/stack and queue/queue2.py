class queue:
    
    def __init__(self,size):
        self.sp=-1
        self.size=size
        self.stack_list=[]
    def overflow(self):
        return self.sp==self.size-1
    def enqueue(self,data):
        if self.overflow():
            print("queue overflow")
        else:
            self.stack_list.append(data)
            self.sp=self.sp+1
            print("data added to stack")
        
    def underflow(self):
        return self.sp==-1
    def dequeue(self):
        if self.underflow():
            print("stack underflow")
        else:
            self.stack_list.pop(0)
            self.sp=self.sp-1
            print("data removed from stack")
    def traverse(self):
        print(self.stack_list)
n=int(input("enter the size of queue"))
s1=queue(n)
while True:
    print('''enter 1 for enqueue ,
enter 2 for dequeue
enter 3 for traverse
enter 4 for exit''')
    operation=int(input())
    if operation==1:
        value =int(input("enter the push value"))
        s1.enqueue(value)
    elif operation==2:
        s1.dequeue()
    elif operation==3:
        s1.traverse()
    elif operation==4:
        print("exiting program")
        break
    else :
        print("invalid input")