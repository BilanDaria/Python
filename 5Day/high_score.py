student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

max_score = -1

for i in student_scores:
    if max_score < i:
        max_score = i

print(f"The highest score in the class is: {max_score}")
