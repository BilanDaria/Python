# fruits = ["apple", 'peach', 'pear']
#
# for i in fruits:
#     print(i)
#     print(i + " Pie")
#
# print(fruits)

# Average height
student_height = input().split()
for i in range(0, len(student_height)):
    student_height[i] = int(student_height[i])

# Easiest way
# result = sum(student_height, 0)/len(student_height)
# print(result)

# the requirements are don't use sum() and len()
height_sum = 0
list_length = 0

for i in student_height:
    height_sum += i
    list_length += 1


print(f"total height = {height_sum}\n"
      f"number of student = {list_length}\n"
      f"average height = {round(height_sum / list_length)}")
