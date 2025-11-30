class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    return root  

def inOrder(root, stack, queue):
    if root is None:
        return
    inOrder(root.left, stack, queue)
    print(root.value, end=" ")  
    stack.append(root.value)
    queue.append(root.value)
    inOrder(root.right, stack, queue)


def insertNumber(root, stack, queue):
    print("\n---- INSERT NUMBERS TO BUILD BINARY SEARCH TREE ----")
    while True:
        uin = input("\nEnter a number (or 'done' to finish): ")
        if uin.lower() == 'done':
            break
        try:
            value = int(uin)
            root = insert(root, value)
        except ValueError:
            print("Invalid! Enter an integer or 'done'.")

    if root is None:
        print("No numbers inserted. Tree is empty.")
    else:
        print("\nIn-order Traversal (Sorted):")
        inOrder(root, stack, queue)

    return root

def main():
    root = None
    stack = []
    queue = []

    root = insertNumber(root, stack, queue)
    
    # MENU SYSTEM
    while True:
        print("\n===== MENU =====")
        print("1. Pop from Stack (LIFO)")
        print("2. Dequeue from Queue (FIFO)")
        print("3. View Stack")
        print("4. View Queue")
        print("5. Insert Number")
        print("6. Exit")

        choice = input("Choose (1-6): ")
        match choice:
            case "1":
                if stack:
                    print("Popped:", stack.pop())
                else:
                    print("Stack empty!")
            case "2":
                if queue:
                    print("Dequeued:", queue.pop(0))
                else:
                    print("Queue empty!")
            case "3":
                print("Stack (top to bottom):", list(reversed(stack)))
            case "4":
                print("Queue (first to last):", queue)
            case "5":
                root = insertNumber(root, stack, queue)
            case "6":
                print("\nProgram ended...")
                break 
            case _:
                print("Invalid! Only Choose 1-6.")

main()