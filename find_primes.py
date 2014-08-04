from is_prime import *

def find_primes(n):

    numbers = [2] 

    for i in range(3, n + 1):
        if i % 2 != 0:
            numbers.append(i) 


    for number in numbers:
        is_prime(number) 







find_primes(int(raw_input("I will find all the prime numbers, from 2 to...  ")))


