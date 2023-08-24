def NthPrime(n):
    primes = []
    i = 1
    while (True):
        i+=1
        status = True
        for j in range(2,int(i/2)+1):
            if(i%j==0):
                status = False
                break
        if(status==True):
            primes.append(i)
        if(len(primes)==n):
            break
    return primes

while True:
    try:
        n = int(input("Enter n to find nth prime number: "))

    except:
        ValueError
    if n <= 0:
        print("Wrong value. Please enter a valid number.")
        print("\n")
    else:
        break