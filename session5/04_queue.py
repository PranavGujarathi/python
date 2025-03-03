import sys

class Queue:
    def __init__(self):
        self.queue_list = []  # Instance variable for the queue

    def enqueue(self, value):
        self.queue_list.append(value)
        print(f"{value} added to the queue.")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! Cannot perform dequeue operation.")
        else:
            removed = self.queue_list.pop(0)
            print(f"Dequeued element: {removed}")

    def front(self):
        if self.is_empty():
            print("Queue is empty! No front element.")
        else:
            print(f"Front element: {self.queue_list[0]}")

    def delete(self):
        self.queue_list.clear()
        print("Queue deleted successfully.")

    def is_empty(self):
        return len(self.queue_list) == 0

    def display(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            print("Queue elements:", self.queue_list)


# Queue operations
obj = Queue()
print("Queue has been created.")

while True:
    print("\n1. Enqueue (Insert element)")
    print("2. Dequeue (Remove front element)")
    print("3. Front (View front element)")
    print("4. Delete queue")
    print("5. Display queue")
    print("6. Exit")

    try:
        ch = int(input("Enter your choice: "))

        if ch == 1:
            value = int(input("Enter value to enqueue: "))
            obj.enqueue(value)
        elif ch == 2:
            obj.dequeue()
        elif ch == 3:
            obj.front()
        elif ch == 4:
            obj.delete()
        elif ch == 5:
            obj.display()
        elif ch == 6:
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
