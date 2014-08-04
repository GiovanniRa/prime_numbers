import math

def eratosthenes_sieve(n):
    numbers_list = []
    position = 1

    for number in range(2, n + 1):
        if number % 2 != 0 or number == 2:
            numbers_list.append(number)
    
    while numbers_list[position] <= math.sqrt(n):
        for x in numbers_list:
            if x > numbers_list[position]:
                if x % numbers_list[position] == 0:
                    numbers_list.remove(x)

        position += 1

    for element in numbers_list:
        print element








eratosthenes_sieve(int(raw_input("Find prime numbers up to ...  ")))  
