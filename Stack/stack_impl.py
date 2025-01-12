from collections import deque
stack=deque()



stack.append(12)
stack.append(15)
print(stack.pop())
stack.append("hello")
stack.append("12.55")

# print(stack)
print(stack.pop())