students_height = input("students score go here").split()
for n in range(0, len(students_height)):
    students_height[n] = int(students_height[n])
print(f"the students list is {students_height}")

total_height = 0
for height in students_height:
    total_height += height

print(f"the total height is{total_height}")

total_number = 0
for number in students_height:
    total_number += 1

print(f"the total number of students is {total_number}")

average_height = round(total_height / total_number)

print(f"the average height is {average_height}")
