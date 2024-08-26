def is_palindrome(n):
    return str(n) == str(n)[::-1]

def find_palindrom(n):
    left = n
    right = n
    while True:
        if is_palindrome(left):
            return left
        elif is_palindrome(right):
            return right
        left -=1
        right +=1
n = int(input())
cert_value = find_palindrom(n)
print(f"Номинал сертификата: {cert_value}")
