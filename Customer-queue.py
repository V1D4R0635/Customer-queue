from collections import deque

class GroceryQueue:
    def __init__(self):
        self.queue = deque()

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, customer):
        self.queue.append(customer)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        else:
            print("The queue is empty, no customer to process.")

    def size(self):
        return len(self.queue)

    def display_queue(self):
        if self.is_empty():
            print("The queue is empty.")
        else:
            print("Current queue:", list(self.queue))

def main():
    grocery_queue = GroceryQueue()
    while True:
        print("\n1. Add customer to the queue")
        print("2. Process customer from the queue")
        print("3. Display current queue")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            customer = input("Enter customer's name: ")
            grocery_queue.enqueue(customer)
            print(f"{customer} has been added to the queue.")
        elif choice == '2':
            customer = grocery_queue.dequeue()
            if customer:
                print(f"{customer} has been processed.")
        elif choice == '3':
            grocery_queue.display_queue()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
