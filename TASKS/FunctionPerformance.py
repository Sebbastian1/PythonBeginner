import time

def function_performance(func, arg, oper, how_many_times = 1):
    sum = 0

    for i in range(0, how_many_times):
        start = time.perf_counter()
        func(arg, oper)
        end = time.perf_counter()
        sum = sum + (end - start)
    return sum

def check_value(value, container):
    return value in container

setContainer = {i for i in range (1000)}
listContainer = [i for i in range (500)]


x = int(input("Podaj wartość = "))

print(check_value(x, setContainer))
print(check_value(x, listContainer))

print(function_performance(check_value, x, setContainer, how_many_times= 500000))
print(function_performance(check_value, x, listContainer,  how_many_times= 500000))