#implementation of stack using array in python

size = int(input("Enter the range of stack : "))

stack = [None] * size   
top = -1                

# push the elements in it
for i in range(size):
    x = int(input("Enter the value to push in stack : "))
    top = top + 1
    stack[top] = x

print("\nThe stack is : ", stack)
print("\nThe top element of the stack is : ", stack[top])

# pop the element 
popped = stack[top]
stack[top] = None
top = top - 1

print("\nThe popped element is : ", popped)
print("\nAfter popping, the stack is : ", stack[:top + 1])
print("\nTop of stack is : ", stack[top])