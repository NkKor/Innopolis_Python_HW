def get_squares_sum(arr):
    sum_squares = 0
    for num in arr:
        sum_squares += num ** 2
    return sum_squares
print(get_squares_sum(list(map(int, input().split()))))
