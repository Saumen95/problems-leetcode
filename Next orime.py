def prime_factor(num):
    factors = []
    for x in range(1, num + 1):  #  implementing euclid algo
        if num % x == 0:
            factors.append(x)

    return factors


def is_prime(num): # check the num if prime or return false
    return len(prime_factor(num)) == 2


def next_prime(num): #  finds next prime
    next_num = num + 1
    while not is_prime(next_num):
        next_num += 1

    return next_num