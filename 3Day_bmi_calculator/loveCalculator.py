print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
full_name = name1 + name2

counter_for_true = 0
counter_for_love = 0

for i in "TRUE":
    counter_for_true += full_name.upper().count(i)

for i in "LOVE":
    counter_for_love += full_name.upper().count(i)

for i in "TRUE":
    counter_for_true += name1.upper().count(i)
    counter_for_true += name2.upper().count(i)
print(counter_for_true)

for i in "LOVE":
    counter_for_love += name1.upper().count(i)
    counter_for_love += name2.upper().count(i)
print(counter_for_love)

total = int(str(counter_for_true) + str(counter_for_love))

if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total >= 40 and total <= 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")

