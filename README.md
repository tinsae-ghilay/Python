# Python
## practice test
``` Python
# Implementieren Sie in dieser Zelle Ihr gesamtes Programm. 
# Code außerhalb dieser Zelle wird bei der Bewertung nicht berücksichtigt.
# Die Funktion A soll Ihre Lösung als Integer zurückgeben.
# Sie können zusätzlich noch beliebig viele Unterfunktionen definieren

# start with prime
def is_prime(n):
    if n <= 3: 
        # if less than 4, it has to be greater than 1 (2 and 3)
        return n > 1
    # eliminate multiples of 2 and 3
    if n % 2 == 0 or n % 3 == 0:
        return False

    # any number that doesnt have a factor 
    # below it's square root, wont have any 
    lim = int(n**0.5)+1
    for i in range(5, lim, 6):

        if n % i == 0 or n % (i+2) == 0:
            return False
    return True

# get list of primes
def getPrimes(l,h):
    primes = []
    for i in range(l,h+1):
        if is_prime(i):
            primes.append(i)

    return primes

def no_six(n):
    res = True
    while n:
        if n%10 ==6:
            return False
        n= n//10
    return res

def isBalance(a,b,c):
    #print( " checking", b)
    mean = (a+c)/2 == b
    
    balance = b-a == c-b
    return mean and no_six(b)



def A(n, m):
    # DEINE ANTWORT HIER
    
    primes = getPrimes(n,m)
    sum = 0

    for i in range(len(primes)-1):
        #print( " checking", primes[i])

        balance = isBalance(primes[i-1],primes[i],primes[i+1])
        if balance:
            #print("is balance ", primes[i])
            sum += primes[i]
    return sum
```
## Code snipets for Programming course WS/23

### Factorial

``` python
def factorize(n):
    res = 1
    for i in range(2,n+1):
        res = res*i
    return res
```
### Prime numbers

#### Is a number prime?
``` Python
# code from wikipedia
def is_prime(n):
    if n <= 3: 
        # if less than 4, it has to be greater than 1 (2 and 3)
        return n > 1
    # eliminate multiples of 2 and 3
    if n % 2 == 0 or n % 3 == 0:
        return False

    # any number that doesnt have a factor 
    # below it's square root, wont have any 
    lim = int(n**0.5)+1
    for i in range(5, lim, 6):

        if n % i == 0 or n % (i+2) == 0:
            return False
    return True
```
#### N<sup>th</sup> prime number
``` python
def get_nth_prime(n):
    # count number of primes found,
    # and see if digit is a prime number
    count,digit = 1,1
    
    while count <= n:
        digit+=1
        if is_prime(digit):
            # increase primes count if one is found
            count+=1
    return digit
```
### Factors and multiples
#### Prime factor
``` Python
def largest_prime_factor(n):
    # Initialize the divisor as the smallest prime number
    i = 2
    # While the square of the divisor is less than or equal to n 
    while i * i <= n:  
        if n % i:  # If n is not divisible by i
            i += 1  # Increment i to check the next number
        else:
            n //= i  # If n is divisible by i, divide n by i
    # The remaining value of n is the largest prime factor
    return n 
```
#### Greatest common factor
``` python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
```
#### Least common multiple
``` Python
def lcm(a, b):
    return abs(a * b) // gcd(a, b)
```
#### Smallest multiple 
``` python
def smallestMultiple(n):
    ans = 1
    for i in range(1, n + 1):
        ans = lcm(ans, i)
    return ans
```

### Sums
#### Sum of multiples of 3 or 5
``` Python
def sum_of_multiples(limit):
    total = 0 
    for i in range(limit):
        # Check if the number is divisible by 3 or 5
        if i % 3 == 0 or i % 5 == 0:
            # Add the number to the total sum 
            # if it is a multiple of 3 or 5
            total += i 
    return total
```
#### Sum of even fibonacci numbers
``` Python
def sum_even_fibonacci(limit):
    # first two terms of the Fibonacci sequence
    # for which addition makes a difference
    a, b = 1, 2
    total = 0
    while a <= limit:
        if a % 2 == 0:
            # Add the term to the total sum if it is even
            total += a
        # Update the terms to the next two in the sequence
        a, b = b, a + b

    return total 
```
### Fibonacci sequence
#### Is a number in Fibonacci sequence?
``` python
def is_perfect_square(n):
    # According to some one named Kurt Mager in Quora, @ https://qr.ae/pKMa62
    # All perfect squares greater than 0 are the sum of consecutive odd numbers.
    # eg, 25 = 1+3+5+7+9, 16 = 1+3+5+7 and so on.
    # additional info, let the biggest number be x,
    # then (x//2)+1 is the square root of n. 
    res, odd = 0, 1
    is_perfect_square = False
    while res < n:
        res += odd
        if res == n:
            #print("square root of ", str(n)+" is "+str((odd+1)/2))
            is_perfect_square = True
        odd+=2
    
    return is_perfect_square

# checks if a number n is a febonacci
# this method is slow for iterration
# so only to be used to check if a number is in the feboncci sequence
def is_fibonacci(n):
    # according to a sentence under the title Identification on wikipedia(link beloow)
    # @ https://en.wikipedia.org/wiki/Fibonacci_sequence#Recognizing_Fibonacci_numbers
    # Binet's formula provides a proof that a positive integer x is Fibonacci 
    # if and only if 5x^2+4 or 5x^2-4 is a perfect square.
    # so we can check for them. 
    r = 5+(n**2)
    return is_perfect_square(r+4) or is_perfect_square(r-4)

```
#### Fibonacci sequence
``` python
# ATTENTION! function does not depend on above function to identify fibonacci number
# populates a list by appending (last+ prevous) item to list
def fibonacci_seq(n):
    n=n-1
    res=[0,1,2]
    for i in range(2,n):
        res.append(res[i-1]+res[i])
    return res
```

### Palindrome numbers

functions may depend on one another or not. attention needed

#### Reverse a number
``` python
# reversing an integer
# int reversed tni ;-)
def tni(n):
    # reversed num ;-)
    mun = 0
    while n:
        # on each loop, modulo 10 gives us the last digit in a number
        # eg. 125 => %10 = 5-> *10 = 50, rest 12 % 10 = 2 add to mun = 52 
        # then *10 =520 +1 = 521
        mun = mun * 10 + (n % 10)
        n = n // 10
    return mun
```
#### Is number Palindrom
``` Python
def is_palindrome(n):
    return n == tni(n)
```
#### Is number a Mirp?

``` Python
def is_mirp(n):
    return is_prime(n) and not is_palindrome(n) and is_prime(tni(n))
```
#### Get mirps in a range

``` Python
def get_mirps(m,n):

    mirps = []

    for i in range(m,n):
        if is_mirp(i):
            mirps.append(i)
    return mirps
```

## Sorting Algorithms

#### Bubble sort 
``` Python
'''
Bubble sort
 source of algorithm @ https://en.wikipedia.org/wiki/Bubble_sort
 improved version to skip over sorting items with same value
'''
sack = [4,2,6,8,9,3,4,6,7,1,0,-3,-7]
def bubble_sort(array,asc):

    if len(array) == 0:
        return None
    
    seeds = len(array)
    while seeds >= 1: # while unsorted seeds remain
        seed = 0 # sorted grain 
        for grain in range(1,seeds):
            #print("trying at position", str(grain))
            if asc and array[grain-1] > array[grain]: # ascending?
                # swap position 
                array[grain-1],array[grain] = array[grain], array[grain-1]
                #print("swapped ",str(array[grain-1])+" with "+str(array[grain]))
                seed = grain # set sorted position as last
            elif not asc and array[grain-1] < array[grain]: # descending
                array[grain-1],array[grain] = array[grain], array[grain-1]
                #print("swapped ",str(array[grain-1])+" with "+str(array[grain]))
                seed = grain # set sorted position as last
        # make loop start from last sorted instead of repeating all the way
        seeds = seed 
    return array
```
#### Selection sort

``` Python
# selection sort taken from home work 
''' 
Context gelernt: und,
Quelcode von Java zu Python adaptiert(Übersetzt)von:
"Selection Sort – Algorithmus, Quellcode, Zeitkomplexität",
@ https://www.happycoders.eu/de/algorithmen/selection-sort/
von Sven Woltmann – 25. Juni 2020 
'''

def selection_sort(array, asc): 

    if len(array) == 0:
        return None
 
    for i in range(len(array)-1):
        
        # hier nehmen wir an, das das element[i] das kleinste bzw großte ist
        seed = i
            
        # und wir vergleichen es mit rest elemente 
        for grain in range(i+1, len(array)):
                
            # sortieren wir ascending? suchen wir ein element der kleiner wie unsere seed ist
            if asc and array[grain] < array[seed]:
                    
                #kleiner element gefunden? wir merken dieser Index
                seed = grain
            #oder descending? suchen wir dann, ein element der größer als unsere seed ist
            elif not asc and array[grain] > array[seed]:
                    
                # größere Element gefunden? wir merken der Index hier.
                seed = grain
                    
        # fals wir kleiner Element gefunden haben, vertauschen wir es mit unsere gemerkte seed
        if seed != i:
            array[i],array[seed] = array[seed],array[i]
    # sortierte list.
    return array
```
#### Insertion sort
``` Python
# insertion sort based on pseudo code 
#@ https://en.wikipedia.org/wiki/Insertion_sort

def insertion_sort(array,asc):
    if len(array) == 0:
        return None
    
    start = 1 # we start from 1 work our way up to the last
    while start < len(array):
        base = start # starting index of our sorting loop
        while base > 0: # compare item to items below it 
            if asc and array[base-1] > array[base]: # Ascending?
                # if smaller swap it
                array[base-1] , array[base] = array[base] , array[base-1]
            elif not asc and array[base-1] < array[base]: #Descending?
                #if its bigger swap it
                array[base-1] , array[base] = array[base] , array[base-1]
            base -= 1# reduce index to compare by 1
        start += 1# increase our starting position
    return array
```

#### Quick sort

``` python
# bellow are needed for quick sort
# quick sort is complicated, I had to look at wikipedia
# @ https://en.wikipedia.org/wiki/Quicksort - read it, try to understand it.
# and then look at implementations @ https://www.javatpoint.com/quick-sort.
# Java version was understandable as I know the syntax already.
# and write code step by step. was worth it!!!!

# here we do sorting of half? of the partition?
def partition (array, start, end, asc):

    # comparison starts between beginning and end elements
    base = start-1
    pivot = array[end]
    for i in range (start,end):
        # current element is at iterating position
        # If current element is smaller than or equal to the pivot(final element)
        # ascending and pivot is bigger than current elemnt?  
        if asc and array[i] < pivot:
            # move item towards pivot position
            base += 1
            array[base], array[i] = array[i], array[base]

        # discending and pivot is smaller than current elemnt?
        elif not asc and array[i] > pivot:
            # move item towards pivot position
            base += 1
            array[base], array[i] = array[i], array[base]
    # no idea why this is happening?
    
    array[base+1], array[end] = array[end], array[base+1]

    return base+1

def sort_quick(array,start, end,asc):
    if len(array) == 0:
        return None
    
    if start < end:
        # devide array in to 2 partitions
        # and sort it
        part = partition(array, start, end,asc)
        sort_quick(array,start,part-1,asc)
        sort_quick(array,part+1,end,asc)

# birds eye view of the function. every thing above this
# is based on fore mentioned resources
def quick_sort(array,asc):
    start , end =0 , len(array)-1
    sort_quick(array,start, end,asc)
    
    return array
```





