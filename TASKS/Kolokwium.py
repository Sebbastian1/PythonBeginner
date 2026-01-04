temperatures = [15, -2, 0, 12, -15, -18, 7]

count_minus = 0
for element in temperatures:
    if element < -10:
        count_minus+=1
print(count_minus)


for i in range(len(temperatures)):
    if temperatures[i] < 0:
        temperatures[i] = 0    
print(temperatures)

tempAvg = 0
for i in temperatures:
    tempAvg+=i
x = tempAvg / len(temperatures)
print(x)


