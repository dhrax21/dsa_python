def get_squared_num(numbers):
    square = []
    for n in numbers:
        square.append(n * n)
        return square

numbers={5,7}
listt=get_squared_num(numbers)
print(listt)
