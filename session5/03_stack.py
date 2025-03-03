import sys
class Stack:
    def __init__(self):
        self.stack_list = []  # Instance variable for the stack

    def push(self, value):
        self.stack_list.append(value)
        print(f"{value} pushed to stack.")
    
    def pop(self):
        if self.is_empty():
            print("Stack is empty! Cannot perform pop operation.")
        else:
            removed = self.stack_list.pop()
            print(f"Popped element: {removed}")

    def peek(self):
        if self.is_empty():
            print("Stack is empty! No top element.")
        else:
            print(f"Top element: {self.stack_list[-1]}")

    def delete(self):
        self.stack_list.clear()
        print("Stack deleted successfully.")

    def is_empty(self):
        return len(self.stack_list) == 0

    def display(self):
        if self.is_empty():
            print("Stack is empty!")
        else:
            print("Stack elements:", self.stack_list)


# Stack operations
obj = Stack()
print("Stack has been created.")

while True:
    print("\n1. Push (Insert element)")
    print("2. Pop (Remove top element)")
    print("3. Peek (View top element)")
    print("4. Delete stack")
    print("5. Display stack")
    print("6. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        value = int(input("Enter value to push: "))
        obj.push(value)
    elif ch == 2:
        obj.pop()
    elif ch == 3:
        obj.peek()
    elif ch == 4:
        obj.delete()
    elif ch == 5:
        obj.display()
    elif ch == 6:
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 6.")

