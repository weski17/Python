import random


array= [5,9,12,1,2,82]


def quick_sort(arr):
    #check if the array has more than one element
    if len(arr) <= 1:
        return arr
    #setting the pivot element and creating the list for letf and right
    pivot = arr[0]
    left = []
    right = []

    #depending on the rellation to the pivot element, the elemnt is sorted in the left or right list
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    #Rekursion
    left = quick_sort(left)
    right = quick_sort(right)

    #Combins the value of the left, pivot and right elments
    return left + [pivot] + right


print(quick_sort(array))

"""
Die durchschnittliche Laufzeit des Quick-Sort-Algorithmus ist O(n*log(n)),
aber im schlechtesten Fall (wenn das Pivot-Element immer das größte oder das kleinste Element ist) 
kann die Laufzeit bis zu O(n^2) betragen.
"""

