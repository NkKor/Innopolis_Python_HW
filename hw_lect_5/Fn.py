"""так и не удалось отладить программу, чтобы она не выдавала ошибки переполнения рекурсивных вызовов.
Пример решения самой функции нашел на GitHub, собрал по образцу конструкцию из try\except,
 но так и не смог отловить почему она продолжает вычислять F(n) при n = None.
 Просьба как нибудь мне намекнуть где я налажал"""
def F(n):
    try:
        if n< 5:
            return n
        elif n % 3 == 0:
            return n + F(n // 3 + 2)
        else:
            return n + F(n + 3)
    except RecursionError:
        print("Ошибка: достигнуто максимальное количество рекурсивных вызовов.")
        return None


def find_min_n():
    n = 5
    while True:
        try:
            if F(n) > 1000:
                return n
            n += 1
        except RecursionError:
            print(f"Ошибка: достигнуто максимальное количество рекурсивных вызовов.")
            return None


min_n = find_min_n()
if min_n is not None:
    print("Минимальное значение n:", min_n)
else:
    print("Ошибка: не удалось найти подходящее значение n.")
