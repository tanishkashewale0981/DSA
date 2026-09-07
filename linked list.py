class Node:
    def __init__(self,data):
        self.data = data
        self.next = None #its by default none
class LL:
    def __init__(self):
        self.head = None 
    def create(self):
        n = int(input(("Enter number of nodes:")))
        if n<=0:
            print("Please enter valid no. of nodes")
        for n in range(1,n+1):
            val = int(input("Enter data for node:"))
            self.insert(val)
    def insert(self,val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node 
    def delete(self):
        num = int(input("Enter value to delete:"))
        if self.head is None:
            print("List is empty.")
            return 
        if self.head.data == num:
            self.head = self.head.next
            print("Node deleted")
            return 
        prev = None
        temp = self.head
        while temp is not None and temp.data !=num:
            prev = temp
            temp = temp.next
        if temp is None:
            print("Node is not found")
            return
        prev.next = temp.next
        print("Node deleted")
    def show (self):
        if self.head ==None:
            print('Nothing to print...')
            return 
        temp = self.head
        while temp is not None:
            print(f"{temp.data}",end="=>")
            temp = temp.next
       
list1 = LL()
while True:
    choice = int(input("\n1.Create\n2.insert\n3.Delete\n4.Show\nEnter your choice:"))
    if choice ==1:
        list1.create()
    elif choice ==2:
        val = int(input("Enter data for node:"))
        list1.insert(val) 
    elif choice ==3:
        list1.delete()  
    elif choice ==4:
        list1.show()
    elif choice ==5:
        print("__Exit__")
        break
    else:
        print("Invalid choice")