
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
print("------------------- Bubble --------------------------")
print(" Ascending ", bubble_sort(sack, True))
print("Discending ", bubble_sort(sack, False))



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

print("------------------ Selection ------------------------")
print(" Ascending ", selection_sort(sack, True))
print("Discending ", selection_sort(sack, False))

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
print("----------------- Insertion -------------------------")
print(" Ascending ", insertion_sort(sack, True))
print("Discending ", insertion_sort(sack, False))

# bellow are needed for quick sort
# quick sort is complicated, I had to look at wikipedia
# @ [[https://en.wikipedia.org/wiki/Quicksort | wikipedia]] - read it, try to understand it.
# and then look at implementations (Java version) was understandable as I know the syntax already.
# @ https://www.javatpoint.com/quick-sort and write code step by step. was worth it!!!!

# here we do sorting of half? of the partition?
def partition (array, start, end, asc):

    # comparison starts between beginning and end elements
    base = start-1
    pivot = array[end]
    for i in range (start,end):
        # current element is at iterating position
        # If current element is smaller than or equal to the pivot(final element)  
        if asc and array[i] < pivot:# ascending and pivot is bigger than current elemnt
            # move item towards pivot position
            base += 1
            array[base], array[i] = array[i], array[base]

        elif not asc and array[i] > pivot:# discending and pivot is smaller than current elemnt
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

print("----------------- Quick sort -------------------------")
print(" Ascending ", quick_sort(sack, True))
print("Discending ", quick_sort(sack, False))




    
    


