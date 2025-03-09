result = 0

# for i in range(1, 11):
#     print(i)

# for i in range(1, 11, 3):   # (start_number, max_number + 1, step)
#     print(i)
#
# for i in range(1, 101):
#     result += i
# print(result)

# Adding Even Number
target = int(input())
even_number_sum = 0

if target >= 0:
    for i in range(0, target+1, 2):
        even_number_sum += i

    print(even_number_sum)
else:
    print("Oops, smth goes wrong!")
