def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_prime_numbers(n):
    for num in range(n + 1):
        if is_prime(num):
            print(num)


n = int(input("Enter a number: "))
print("Prime numbers from 0 to", n, "are:")
print_prime_numbers(n)
