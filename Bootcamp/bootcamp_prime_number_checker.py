def prime_checker(number):
    for x in range(2, int(n**0.5) + 1):
        if number % x == 0:
            return False
    return True
    
n = int(input("Check this number: "))
(prime_checker(number=n))
if prime_checker(number=n) is False:
  print("It's not a prime number")
else:
  print("It's a prime number")