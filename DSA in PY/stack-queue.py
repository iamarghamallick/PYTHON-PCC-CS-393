# Stack using list
stack = []


# Function to print top element of stack
def peek(stack):
    if stack != []:
        print(stack[-1] + " is top element")
    else:
        print("Stack Empty!!!")


# Function to print size of stack
def size(stack):
    print("Size of stack is " + str(len(stack)))


# Function to check if a stack is empty
def Isempty(stack):
    if stack == []:
        print("Isempty() status is True")
    else:
        print("Isempty() status is False")


# append() function is used to push element in the stack
stack.append("a")
stack.append("b")
stack.append("c")
stack.append("ddd")
size(stack)
print(stack)
peek(stack)
# pop() function to pop element from stack in LIFO order
print(stack.pop() + " is popped")
print(stack)
Isempty(stack)
print(stack.pop() + " is popped")
print(stack.pop() + " is popped")
print(stack)
Isempty(stack)
print(stack.pop() + " is popped")
Isempty(stack)
