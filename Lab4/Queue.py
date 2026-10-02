# implermentation of queue using array in python

size = int(input("Enter value for range : "))

queue = [None] * size   # fixed size array
front = 0               # points to the first element
rear = -1               # points to the last element

# enqueue
for i in range(size):
    y = int(input("Enter the value to push in queue : "))
    rear = rear + 1
    queue[rear] = y

print("\nThe queue is : ", queue[front:rear + 1])

# dequeue
dequeued = queue[front]
queue[front] = None
front = front + 1

print("\nThe popped element is : ", dequeued)
print("\nThe queue after popping is : ", queue[front:rear + 1])

# dequeue again
dequeued = queue[front]
queue[front] = None
front = front + 1

print("\nThe popped element is : ", dequeued)