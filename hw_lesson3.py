# Урок 3 Задача 1 ---------------------------------------------------
def format_name(full_name) -> str:
    parts = full_name.split()
    last_name = parts[0]
    first_name = parts[1]
    if len(parts) > 2:
        middle_name = parts[2]
        return f"{last_name} {first_name[0]}.{middle_name[0]}."
    else:
        return f"{last_name} {first_name[0]}."
print(format_name(input()))

# Урок 3 Задача 2 ---------------------------------------------------
def format_name(full_name) -> str:
    parts = full_name.split()
    last_name = parts[0]
    first_name = parts[1]
    if len(parts) > 2:
        middle_name = ""
        for i in range(2, len(parts)):
            middle_name += parts[i][0] + "."
        return f"{last_name} {first_name[0]}.{middle_name}"
    else:
        return f"{last_name} {first_name[0]}."
print(format_name(input()))

# Урок 3 Задача 3 ---------------------------------------------------
students=[
    {"id":367673,"full_name":"ЯрцевВалерийРустэмович"},
    {"id":563234,"full_name":"ШиптенкоВиталийПрограммирович"},
    {"id":982123,"full_name":"ДатабейзовИванДжетлагович"},
]
def give_license(student_id: int) ->bool:
    global students    
    for element in students:
        for value in element.values():
            if value == student_id:
                return True
            else:
                return False
print(give_license(int(input())))

# Урок 3 Задача 4 ---------------------------------------------------
n = int(input())
m = []
for i in range(0,n):
    m.append(int(input())) 
def fibo(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
for i in range(0,n):
    print(f"Порядковый номер числа - {m[i]}, значение - {fibo(m[i])}")

# Урок 3 Задача 5 ---------------------------------------------------
def fibo_decorator(func):
    memory = {}
    def wrapper(n):
        if n in memory:
            return memory[n]
        else:
            result = func(n)
            memory[n] = result
        return result
    return wrapper
n = int(input())
m = []
for i in range(0,n):
    m.append(int(input())) 
@fibo_decorator
def fibo(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
for i in range(0,n):
    print(f"Порядковый номер числа - {m[i]}, значение - {fibo(m[i])}")
