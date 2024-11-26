my_range = range(3, 21)
num_range = range(1,21)
result = ''

for i in my_range:
    for j in range(1, i): # 1 num
        for k in range(j + 1, i): # 2 num
            if i % (j + k) == 0:
                result += f'{j}{k}'

    print(f'{i} - {result}')
    result = ''
