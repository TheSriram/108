import math

def primenumberseive(n):
    prime_list = [i for i in range(2, n)]
    for i in range(2, int(math.ceil(math.sqrt(n)))):
        count = 0
        while ((i * i) + (i*(count))) <n:
            try:
                prime_list.remove((i * i) + (i*count))
            except ValueError:
                pass
            count = count + 1
    return prime_list
