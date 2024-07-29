import time

start = time.time()
numbers = [i for i in range(1, 1000001)]
squares = []
for number in numbers:
    squares.append(number ** 2)
end_time = time.time()
elapsed_time = end_time - start
print("До исправления:", elapsed_time)

start = time.time()
numbers = range(1, 1000001)
squares = [number ** 2 for number in numbers]
end_time = time.time()
elapsed_time = end_time - start
print("После исправления:", elapsed_time)
