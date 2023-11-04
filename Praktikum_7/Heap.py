heap = []

start = True
def menu():
    while start:
        menu = input("__Auswahlmöglichkeit__\n"
                     "e: Einfügen eines Elements in den Heap\n"
                     "l: Löschen des kleinsten Elements aus dem Heap\n"
                     "s: soritiertes Ausgeben des Heaps(HeapSort)\n"
                     "a: Ausgaben des Arrays\n"
                     "n: erneutes Einlesen der Datei\n")
        if menu == "e":
            paste()
        if menu == "l":
            delete()
        if menu == "s":
            sort(heap)
        if menu == "a":
            printOut()
        if menu == "n":
            readData(heap)

def paste():
    try:
        element = (int(input("Enter element to add: ")))
    except:
        print("Only enter numbers")

    for i in heap:
        if element == i:
            print("Allread in the Heap")
            return
    heap.append(element)
    indexSize = len(heap)
    sortAfterInput(indexSize)

def sortAfterInput(size):

    parentIndex = (size - 1) // 2
    parentValue = heap[parentIndex]

    currentIndex = size - 1
    currentValue = heap[currentIndex]

    if (int(parentValue) > int(currentValue)):
        heap[parentIndex] = currentValue
        heap[currentIndex] = parentValue
        sortAfterInput(parentIndex)

def delete():
    if not heap:
        return
    print("Delete: " + str(heap[0]))
    temp = heap[len(heap) - 1]
    heap[0] = temp
    heap.pop(len(heap) - 1)
    sortFromParent(0)

def heapify(heap, elements, maxIndex):
    parent = maxIndex
    leftChild = 2 * maxIndex + 1
    rightChild = 2 * maxIndex + 2

    if leftChild < elements and heap[parent] < heap[leftChild]:
        maxIndex = leftChild
    if rightChild < elements and heap[maxIndex] < heap[rightChild]:
        maxIndex = rightChild
    if maxIndex != elements:
        heap[elements], heap[maxIndex] = heap[maxIndex], heap[elements]
        heap = heapify(heap,elements,maxIndex)

def sort(list):
    if len(list) <= 1:
        return list
    lenght = len(list)
    for i in range(lenght // 2):
        list = heapify(list, lenght, i)

def sortFromParent(index):
    size = len(heap)
    if 2 * size + 1 > len(heap) - 1:
        return
    parentIndex = index
    parentValue = heap[parentIndex]

    childIndexLeft = 2 * index + 1
    childValueLeft = heap[childIndexLeft]

    childIndexRight = 2 * index + 2
    childValueRight = heap[childIndexRight]

    minChild = childIndexLeft

    if childValueLeft > childValueRight:
        minChild = childIndexRight
    if parentValue > min(childValueLeft, childValueRight):
        heap[minChild] = parentValue
        heap[parentIndex] = min(childValueLeft, childValueRight)
        print(heap)
        sortFromParent(minChild)


def printOut():
    if len(heap) == 0:
        print("Heap empty")
    else:
        print(heap)


def readData(heap):
    datei = input("Enter data Url: ")
    datei += ".txt"

    try:
        datei = open(datei, 'r')
        print("File found")
    except:
        print("File not found")
        return

    for zeile in datei:
        zahl = int(zeile.replace("\n", ""))
        heap.append(zahl)
        indexSize = len(heap)
        sortAfterInput(indexSize)
    datei.close()


menu()
