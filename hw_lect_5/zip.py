def get_normalised(xs: list, ys: list):
    x, y, norm_coord = [], [], []
    if len(xs) == len(ys):
        try:
            x = list(map(lambda i: i-xs[0], xs))
            y = list(map(lambda j: j-ys[0], ys))
            norm_coord = tuple(zip(x, y))

        except Exception as e:
            print("Ошибка:", e)
        else:
            return norm_coord
    else:
        return f"Списки координат не одинаковые"


xs = list(map(int, input().split(",")))
ys = list(map(int, input().split(",")))
print(get_normalised(xs, ys))
