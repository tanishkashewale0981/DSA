class stack:
    def __init__(self):
        self.Top=-1
        self.st=[0]*10

    def push(self,x):
        if self.Top==9:
            print("Stack overflowed")
        else:
            self.Top+=1
            self.st[self.Top]=x
            print(x,"pushed into stack")

    def pop(self):
        if self.Top==-1:
            print("Stack underflow")
            return None
        else:
            x=self.st[self.Top]
            self.Top-=1
            print(x,"popped from stack")
            return x

    def peek(self):
        if self.Top==-1:
            print("Stack is empty")
            return None
        else:
            print("top element of stack is",self.st[self.Top])

    def display(self):
        if self.Top==-1:
            print("Stack is empty....Nothing to display!!!")
            return
        else:
            print("Stack elements are:")
            for i in range(self.Top,-1,-1):
                print(self.st[i])

s=stack()

while True:
    print("\n----------STACK MENU------------")
    print("1. Push")
    print("2. Pop")
    print("3.peek")
    print("4.display")
    print("5. Exit")

    choice=int(input("Enter yuor choice:-"))

    if choice==1:
       x=int(input("Enet the elemnet to be pushed"))
       s.push(x)
    elif choice==2:
       s.pop()
    elif choice==3:
       s.peek()
    elif choice==4:
       s.display()
    elif choice==5:
       print("---Exiting----")
       break
    else:
       print("invalid choice")
       

  

   

    



