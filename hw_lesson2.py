# Урок 2 Задача 1 ---------------------------------------------------
n = int(input())
k = int(input()) - 1 #Так как индексы в списке идут с 0 вычитаем 1
s = input()
chijik_mashr = [ int(i) for i in s.split(' ')]
chijik_mashr.sort()
s = input()
pijik_mashr = [ int(i) for i in s.split(' ')]
pijik_mashr.sort()
s = input()
ksenia_mashr = [ int(i) for i in s.split(' ')]
ksenia_mashr.sort()
if chijik_mashr[k] < pijik_mashr[k] < ksenia_mashr[k]:
    print("Ксюша")
elif chijik_mashr[k] > pijik_mashr[k] > ksenia_mashr[k]:
    print("Чижик")
elif chijik_mashr[k] < pijik_mashr[k] > ksenia_mashr[k]:
    print("Пыжик")
else: print("Ничья")

# Урок 2 Задача 2 ---------------------------------------------------
kol_hh = int(input())
list_hh = []
for i in range(0,kol_hh):
    s = input()
    coord = tuple(int(i) for i in s.split(" "))
    list_hh.append(coord)
print(list_hh)

# Урок 2 Задача 3 ---------------------------------------------------
werbs = {"к":"т","р":"а","и":"к","в":"л","о":"у","я":"ч","з":"ш","ы":"е"}
s = input()
frase = ''
for i in range(0,len(s)):
    if s[i] == " ":
        frase += s[i]
    else: 
        frase += werbs[s[i]]
print(frase)

# Урок 2 Задача 4 ---------------------------------------------------
n = int(input())  # количество студентов
k = int(input())  # количество сочинений
works = []
for i in range(0, n):
    student_works = input().split()
    works.append(set(student_works))
common_works = works[0]
for i in range(1, n):
    common_works = common_works.intersection(works[i])
print(*common_works)

# Урок 2 Задача 5 ---------------------------------------------------
