import logging
import time
import random
import string

def quicksort(arr,save,count,logger):

    # if the array has 1 Elements
    if len(arr) <= 1:
        return arr
    # if the array has 2 Elements
    if len(arr) == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        return arr

    # if the array has 3 Elements
    if len(arr) == 3:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        if arr[1] > arr[2]:
            arr[1], arr[2] = arr[2], arr[1]
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        return arr

    #lists for sorting
    pivot = arr[2]
    less = []
    equal = []
    greater = []

    #if the array has more than 3 Elements:
    for element in arr:
        if element < pivot:
            less.append(element)
        elif element == pivot:
            equal.append(element)
        else:
            greater.append(element)
        if(save):
            count = count +1

    if(save):
        logger.info(f"Pivot: {pivot}")
        logger.info(f"less: {less}")
        logger.info(f"Equal: {equal}")
        logger.info(f"greater: {greater}")

    return quicksort(less,save,count,logger) + equal + quicksort(greater,save,count,logger)

#array = ["Igel", "Zebra", "Affen", "Lama", "Kroko", "T-Rex", "Papagai", "Wildschwein", "Dodo"]
array = [''.join(random.choices(string.ascii_lowercase, k=5)) for _ in range(100)]

def start():
    #switch to activate logging
    save = False
    count = 0
    logger = logging.getLogger("logger")
    c = input("if you want to safe a Logfile enter -> y\n"
              "if not press any other key:")
    if c.lower() == 'y':
        save = True
    if(save):
        # Implement logger
        logger.setLevel(logging.INFO)
        logging.basicConfig(filename="Logfile.txt", filemode="w")
        print("Logging is on")

    go = time.time()
    sorted_array = quicksort(array,save,count,logger)
    end = time.time()
    print(sorted_array)
    print(f"Quicksort runtime: {end - go:.30f} seconds")

start()
