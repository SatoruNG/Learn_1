my_list = input().strip('[]').split(", ") # [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
idx = 0

my_list = list(my_list)
while True:
    if idx == len(my_list):
        break

    if int(my_list[idx]) < 0:
       break

    elif int(my_list[idx]) > 0:
        print(my_list[idx])
        idx += 1
        continue

    else:
        idx += 1
