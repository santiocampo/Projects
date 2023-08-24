while True:
    try:
        n = int(input("Enter n to find nth Fibonacci number: "))

    except:
        ValueError
    if n <= 0:
        print("Wrong value. Please enter a valid number.")
        print("\n")
    else:
        break

n1 = 0
n2 = 1
if n == 1:
    print("The 1st Fibonacci number is: 0")
elif n == 2:
    print("The 2nd Fibonacci number is 1")
else:
    for i in range(2,n):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
    print("The " + str(n) +"nth Fibonacci number is: " + str(n3))