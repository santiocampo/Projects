def PrimeFactors(n):
    factors = []
    i = 2
    while i**2 <= n:
        if n%i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1
    if n >1:
        factors.append(n)
    return factors

while True:
    try:
        n = int(input("Enter a numer to find its prime factors: "))

    except:
        ValueError
    if n <= 0:
        print("Wrong value. Please enter a valid number.")
        print("\n")
    else:
        break