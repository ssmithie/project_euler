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

def smallest_num():
# not solved
    """Problem 5: return smallest number that is divisible by all numbers from 1 to 20"""
    num = 1
    i = 1
    pass

def sum_square_dif(n):
    """Problem 6: difference between sum of squares of first n numbers and the surm of the frist n numbers squared"""
    sum_square = 0
    square_sum = 0
    for i in range(1, n+1):
        sum_square += i**2
        square_sum += i
    return (square_sum ** 2) - sum_square




if __name__ == "__main__":
    print(sum_square_dif(100))
