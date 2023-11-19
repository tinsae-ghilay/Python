def isPrime(n):
    is_prime = n > 1
    for p in range(2,(n//2)+1):
        if n % p == 0:
            is_prime = False
            break

    return is_prime

print(isPrime(17))

def find_nth_Prime(n):
    prime = 0
    iterant = 0
    count = 0
    while count < n :
        if isPrime(iterant):
            prime = iterant
            count+=1

        iterant+=1
    return prime

print(str(find_nth_Prime(100)))



def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def smallestMultiple(n):
    ans = 1
    for i in range(1, n + 1):
        ans = lcm(ans, i)
    return ans

#print(str(smallestMultiple(100)))