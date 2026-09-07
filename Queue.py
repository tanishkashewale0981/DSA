class Queue:
    def __init__(self):
        self.front = -1
        self.rear = -1
        self.q = [0] * 10

    def enqueue(self, x):
        if self.rear == 9:
            print("Queue Overflow")
        else:
            if self.front == -1:
                self.front = 0

            self.rear += 1
            self.q[self.rear] = x
            print(x, "inserted into queue")

    def dequeue(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue Underflow")
            return None
        else:
            x = self.q[self.front]
            self.front += 1
            print(x, "deleted from queue")
            return x

    def peek(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue is empty")
        else:
            print("Front element is:", self.q[self.front])

    def display(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue is empty")
        else:
            print("Queue elements are:")
            for i in range(self.front, self.rear + 1):
                print(self.q[i])


q = Queue()

while True:
    print("\n---------- QUEUE MENU ----------")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        x = int(input("Enter element to insert: "))
        q.enqueue(x)

    elif choice == 2:
        q.dequeue()

    elif choice == 3:
        q.peek()

    elif choice == 4:
        q.display()

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice")