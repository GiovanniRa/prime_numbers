def is_prime(n):
    
    x = True

    if n == 1:
        x = False

    else:
        for i in range(2, n ):
            if n % i == 0:
                x = False
                break
            else:
                x = True

    if x:
        print n






