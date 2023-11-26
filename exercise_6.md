# Recursive functions
### is_odd(n)
Write a function with the signature `is_odd(n)` that takes an `int` as a parameter and returnes a `boolean`
Return value should be `True` if number is Odd, and `False` if not. You should use recursive funktions instead of a loop.
<br>***Atention!*** Use interchanging recursion for your solution 

### Solution ###
``` Python
def mod(n): # this devides a numer by 2
    num = n % 2
    return is_odd(num)# wechselseitige Rekursion
# DEINE ANTWORT HIER
def is_odd(n):
    if n == 1:               # 1 is odd
        return True
    elif n == 0:             # 2 is even(not odd)
        return False
    else:
        return mod(n)        # wechselseitige Rekursion
```

### recursively calculate greatest common factor
implement a programm that calculates the greatest common factor of two numbers, Recursion should be used

### Solution ###
``` Python
def ggt(a,b):
    if a == 0: # if a = 0, we have b as ggT
        return b
    else:
        if b > a: # is b > a, we swap
            a,b = b,a
        a = a - b # we reset value of a
        return ggt(a,b) # and do it again / recursion*
```

### Nested Array.
implement a program, that adds all integer values inside a 3-D array. if there are no integers,
it should return 0, if there are, it should return the sum of all of them. e.g for the array
`[1, [2, [3]], 4.44, [5, ["Hallo", 6]]]` the naswer should be 17 (1 + 2 + 3 + 5 + 6). 
the calculation should happen using recurson in a function `nested_sum(array)`

### Solution ###
``` Python
''' 
    I tried with only the nested_sum(array) function,
    but since it takes only an array, the only solution I could think of
    to update the array, was removing the elements that are already added.
    in the end, the result was correct, rhe array didnt stay as it was. reduced
    to array with 0 elements
    but that was not accepted by validation even though the answer was right.
    so I wrote a second function that takes array and index.
    that way, the array stays as it was, and since index gets updated recursively
    I was able to get the sum of elements
    '''

def add(array, index):
    
    # since length to index is length-1, if length < 0 nothing to add
    # we return 0
    if index < 0: 
        return 0 
    # if there are elements, we check if item is type int and add if it is
    # and call function again i.e 'Primitive Rekursion'
    if type(array[index])== int:
        return array[index]+ add(array, index-1)
    
    # but if item is a nested array, we do a 'Kaskadenförmige Rekursion'
    elif type(array[index]) == list:
        return add(array[index], len(array[index])-1)+ add(array, index-1)
    
    # if its not an int or a list, we do a 'primitve recursion' without adding anything
    else:
        return add(array, index-1)

# function calls a recursive function
def nested_sum(array):
    if len(array) == 0:
        return 0
    else:
        return add(array, len(array)-1)
```

### Exercise from previous years  exam
A function signe `sigma(n)` returns the sum of all numbers that divide n without a remainder
e.g `sigma(4)` 1 + 2 + 4 = 7:<br>
another function `S(m,d)` should then be implemented that returns the sum of all `sigma(i)` : such that i < or = to m
and `sigma(i)` is divisible by d without a remainder

### Solution

``` Python
def sigma(n):
    res = 0

    for i in range(1,n+1):
        if n % i == 0:
            res+=i
    return res

# vor ein paar jahre war die prüfung einfacher wie heuer .;-|

def S(m, d):
    # DEINE ANTWORT HIER
    res = 0
    for i in range(m):
        j = sigma(i)
        if j % d == 0:
            res += j
    return res
```

### Mirp ###

Mirp are prime numbers that are not palindrom but when reversed, they become primes too.
e.g, 113 is a prim, and so is its reverse 311.

Now implement a program that calculates the sum of all Mirp numbers that have exactly two ones, that aare within a range of given integers<br>
e.g. M(100, 1100) = 113 + 311 + 1021 + 1031 + 1061 + 1091 = 4628

### Solution ###

``` Python
# Im sinn des Teile und Herrsche Principle
'''
    1, werden wirp verifizieren weder ein nummer Prime ist oder nicht
    2, werden wir schauen ob der reverse von nummer auch Prime ist
    
                    2.1, für des werden wir nummer in reverse schreiben
                    2.2, schauen ob es ein Palindrome zb.131 ist
                    
    3, ist es ein mirp dann? n ist prime, reverse von n ist auch prime,
       n ist kein Palindrome
    4, sammeln wir, dann alle Mirps in gegebenen Range
    5, implementieren wir dann die summe von Mirps
    
                    5.1, hier schauen wir, ob Mirp genau zwei einser hat.
                         wenn ja, addieren wir des zu Summe
                         
       und geben wir resulat von Nr 5 als rückgabe.
'''

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

def is_palindrome(n):
    return n == tni(n)

def is_mirp(n):
    return is_prime(n) and not is_palindrome(n) and is_prime(tni(n))

def get_mirps(m,n):

    mirps = []

    for i in range(m,n):
        if is_mirp(i):
            mirps.append(i)
    return mirps

def has_two_ones(n):
    count = 0
    while n:
        if n % 10 == 1:
            count += 1
        n = n // 10
    return count == 2

def M(n, m):
    
    # DEINE ANTWORT HIER
    res = 0

    mirps = get_mirps(n,m)

    for mirp in mirps:
        if has_two_ones(mirp):
            res += mirp
    
    return res
```

