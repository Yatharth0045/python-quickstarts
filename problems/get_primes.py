nums = range(2,1000)

def is_prime(number):
    for i in range(2,number):
        if number % i == 0:
            return False
    return True

prime_list = list(filter(is_prime,nums))

print(prime_list)
