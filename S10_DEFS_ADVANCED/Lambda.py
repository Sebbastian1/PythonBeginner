def podwoj(x):
    return x * 2

my_list = [2, 14, 22, 7, 6, 4, 5, 17]

filtered = list(filter(lambda x: x % 2 == 0, my_list))

print(filtered)