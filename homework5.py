import math
MAX_NUMBER = 100


def FizzBuzz_while():
    number = 1
    while number <= MAX_NUMBER:
        if is_prime(number):
            print("Prime")

        elif number % 3 == 0 and number % 5 != 0:
            print("Fizz")

        elif number % 5 == 0 and number % 3 != 0:
            print("Buzz")

        elif number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")

        else:
            print(number)

        number += 1


def FizzBuzz_for():
    for i in range(1, MAX_NUMBER + 1):
        if is_prime(i):
            print("prime")

        elif i % 3 == 0 and i % 5 != 0:
            print("Fizz")

        elif i % 5 == 0 and i % 3 != 0:
            print("Buzz")

        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")

        else:
            print(i)


def is_prime(number):
    """
    Checks if a number is a prime.
    """
    if number == 2:
        return True

    if number < 2 or number % 2 == 0:
        return False

    return check_prime(number)

def check_prime(number):
    """
    Checks if an odd number greater than 1 is a prime.
    """
    for i in range(3, math.ceil(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False

    return True

def count_primes():
    prime_counter = 1
    for i in range(3, MAX_NUMBER + 1, 2):
        if check_prime(i):
            prime_counter += 1
    return prime_counter


#FizzBuzz_for()
print(f"There are {count_primes()} primes below {MAX_NUMBER}!!!")