numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for number in numbers:
    if number < 2 :
        continue
    is_prime = True
    for i in range(2,number):
        if (number % i) == 0:
            is_prime = False
            not_primes.append(number)
            break
    else :
        primes.append(number)
        if is_prime:
            print("not_primes ", not_primes)
        else:
            print("primes ", primes)
