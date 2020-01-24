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
    """Problem 5: return smallest number that is divisible by all numbers from 1 to 20"""
    num = 1
    i = 1
    while i >= 20:
        if num % i == 0:
            i += 1
        else:
            num += 1
            i = 1
    return num

if __name__ == "__main__":
    print(smallest_num())
