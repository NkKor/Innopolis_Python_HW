n = int(input())
grades = list(map(int, input().split()))
even_grades = []
for grade in grades:
    if grade % 2 == 0:
        even_grades.append(grade)
sum_even_grades = sum(even_grades)
average_even_grade = sum_even_grades / len(even_grades)
final_grade = int(average_even_grade)
print(final_grade)
