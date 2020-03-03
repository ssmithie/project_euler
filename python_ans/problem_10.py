#problem 10:

def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def sum_primes(n):
	num = 0
	for i in range(n+1):
		if is_prime(i):
			num += i
			#print(num)
	return num

if __name__ == "__main__":
	print(sum_primes(2000000))