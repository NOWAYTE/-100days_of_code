def prime_checker(number):
    its_prime = True
    for i in range(2, number - 1):
        if number % i == 0:
            its_prime = False

    if its_prime:
        print("its a prime number")
    else:
        print("its not a prime number")


n = int(input("check the number: "))
prime_checker(number=n)
