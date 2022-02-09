def is_prime(number):
    if number == 1:
        return True
    for i in range(2, number - 1):
        if number % i == 0:
            return False
    return True


def get_primes(number):
    i = 1
    while i < number:
        if is_prime(i):
            yield i
        i += 1


for i in get_primes(100):
    print(i)

gen = get_primes(10)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
