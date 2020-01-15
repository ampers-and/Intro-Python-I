# Stretch 3 - isPrime using the sieve of Eratosthenes


def is_prime(x):

    if x > 120:
        return "Must enter number less than 121"

    elif x == 2 or x == 3 or x == 5 or x == 7:
        return True

    elif x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0:
        return False

    else:
        return True


y = int(input("Enter a number 121 to check if it is prime: "))

print(is_prime(y))
