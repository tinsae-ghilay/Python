# Problem 1:
# Find the sum of all the multiples of 3 or 5 below 1000.

def sum_of_multiples(limit):
    total = 0  # Initialize total sum to 0
    for i in range(limit):  # Iterate through numbers from 0 to limit-1
        if i % 3 == 0 or i % 5 == 0:  # Check if the number is divisible by 3 or 5
            total += i  # Add the number to the total sum if it is a multiple of 3 or 5
    return total  # Return the total sum

# Call the function with 1000 as the limit and print the result
result = sum_of_multiples(1000)
print(f"Problem 1 - The sum of multiples is: {result}")


# Problem 2:
# Find the sum of the even-valued terms in the Fibonacci sequence whose values do not exceed four million.

def sum_even_fibonacci(limit):
    a, b = 1, 2  # Initialize the first two terms of the Fibonacci sequence
    total = 0  # Initialize total sum to 0

    while a <= limit:  # Continue loop until the term exceeds the limit
        if a % 2 == 0:  # Check if the term is even
            total += a  # Add the term to the total sum if it is even
        a, b = b, a + b  # Update the terms to the next two in the sequence

    return total  # Return the total sum of even-valued terms

# Call the function with 4000000 as the limit and print the result
print(f"Problem 2 - The sum of even-valued Fibonacci terms is: {sum_even_fibonacci(4000000)}")


# Problem 3:
# Find the largest prime factor of the number 600851475143.

def largest_prime_factor(n):
    i = 2  # Initialize the divisor as the smallest prime number, which is 2
    while i * i <= n:  # While the square of the divisor is less than or equal to n
        if n % i:  # If n is not divisible by i
            i += 1  # Increment i to check the next number
        else:
            n //= i  # If n is divisible by i, divide n by i
    return n  # The remaining value of n is the largest prime factor

# Call the function with 600851475143 as the input and print the result
print(f"Problem 3 - The largest prime factor is: {largest_prime_factor(600851475143)}")


# Problem 4:
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(n):
    return str(n) == str(n)[::-1]  # Check if the number is a palindrome

def largest_3_digit_palindrome():
    largest_palindrome = 0  # Initialize the largest palindrome to 0
    for i in range(100, 1000):  # Iterate over all 3-digit numbers for the first factor
        for j in range(100, 1000):  # Iterate over all 3-digit numbers for the second factor
            product = i * j  # Calculate the product of the two 3-digit numbers
            if is_palindrome(product) and product > largest_palindrome:  # Check if the product is a palindrome and larger than the current largest
                largest_palindrome = product  # Update the largest palindrome
    return largest_palindrome  # Return the largest palindrome found

# Call the function and print the result
print(f"Problem 4 - The largest palindrome made from the product of two 3-digit numbers is: {largest_3_digit_palindrome()}")

# prime numbers
def isPrime(n):
    is_prime = n > 1
    for p in range(2,(n//2)+1):
        if n % p == 0:
            is_prime = False
            break

    return is_prime

print(isPrime(1))

def find_nth_Prime(n):
    prime, count = 1, 0
    while count < n :
        prime +=1
        if isPrime(prime):
            count+=1

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