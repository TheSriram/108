def primenumberseive(n):

    total_list = [i for i in range(2, n)]
    for i in range(2, int(math.sqrt(n))):
        count = 0
        while ((i * i) + (i*(count+1))) <n:
            total_list[(i * i) + (i*count)] = 0
            count = count + 1
    primes = [elem for elem in total_list if elem!=0]
    return primes

