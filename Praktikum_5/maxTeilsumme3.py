import sys
import time


print("Bitte geben Sie den Namen der Textdatei an, welche eine Folge von Integer enthaelt:")
fileRead = 0
file = ""

fileName = input()
try:
    file = open(fileName, "r")
except IOError:
    print("Couldn't find file!")
else:
    fileRead = 1

#  start of counter
timeTaken = time.time()

if fileRead == 1:
    integers = []

    for line in file:
        integers.insert(0, int(line))  # inserts the number into the very front and shifts everything else back

    n = len(integers)  # len() returns the length of an object
    maxSum = -sys.maxsize - 1  # gets the smallest integer number
    start = finish = 0

    additionCounter = 0  # counts additions

    for i in range(1, n):
        for j in range(i, n):
            sum = 0

            for k in range(i, j):
                sum += integers[k]
                additionCounter += 1

            if sum > maxSum:
                maxSum = sum
                start = i
                finish = j

    timeTaken = round(time.time() - timeTaken)

    print("max. Teilsumme:", maxSum)
    print("erster Index:", start)
    print("letzter Index:", finish)
    print(additionCounter, "Additionen durchgeführt")
    print("Verwendete Zeit:", timeTaken, "seconds")  # does work
