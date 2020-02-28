def sum_nat_3_5(num):
    """Problem 1: returns sum of all the multiples of 3 or 5 below given num"""
    ans = 0
    
    for i in range(0, num):
        if i % 5 == 0:
            ans += i
        elif i % 3 == 0:
            ans += i
    return ans

def fib_sequence():
    x = 0
    y = 1
    pass

def sum_even_fibonacci(num):
    """Problem 2: return sum of all even numbers in fibonacci sequence below num"""
    seq = []
    for i in range(1, num):
        pass

def palindrome():
    """Problem 4: return highest palindrome product of two 3-digit numbers"""
    palindromes = []
    for i in range(100, 999):
        for j in range(100, 999):
            num = i*j
            if num == int(str(num)[::-1]):
                palindromes.append(num)
    return max(palindromes)

#Problem 5 - not solved
def smallest_num():
    """return smallest number that is divisible by all numbers from 1 to 20"""
    num = 1
    i = 1
    pass

#Problem 6:
def sum_square_dif(n):
    """difference between sum of squares of first n numbers and the surm of the frist n numbers squared"""
    sum_square = 0
    square_sum = 0
    for i in range(1, n+1):
        sum_square += i**2
        square_sum += i
    return (square_sum ** 2) - sum_square

#Problem 7: - not solved
def find_prime(n):
    """Return the nth prime number"""
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    primes = [2]
    number = 3
    while len(primes) < n:
        print(number)
        if is_prime(number) == True:
            primes.append(number)
            number += 1
        else:
            number += 1
    #if len(primes) == n:
    return primes[-1]

#Problem 8: - not solved
def find_greatest(input_num):
    num = 0
    index = 0
    products = []

    def digit_product(s):
        result = 1
        for c in s:
            result *= int(c)
        return result

    for i in range(len(input_num)-12):
        this_num = input_num[i:(i+13)]
        prod = digit_product(this_num)
        print(prod, this_num)
        products.append(prod)
        if prod > num:
            num = prod
            index = i
            ans = this_num
            # print(num, i)
    return ans

input_num = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"

if __name__ == "__main__":
    print(find_greatest(input_num))
