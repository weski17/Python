import time


def maxTeilsummerek(A, links, rechts):
    if links == rechts:
        return max(A[links], 0)
    m = (links + rechts) // 2
    maxrl = rechtesRandmax(A, links, m)
    maxlr = linkesRandmax(A, m + 1, rechts)
    return max(maxTeilsummerek(A, links, m), maxTeilsummerek(A, m + 1, rechts), maxlr + maxrl)


def rechtesRandmax(A, li, re):
    zwischensumme = 0
    max_summe = 0
    for i in range(re, li - 1, -1):
        zwischensumme += A[i]
        max_summe = max(max_summe, zwischensumme)
    return max_summe


def linkesRandmax(A, li, re):
    zwischensumme = 0
    max_summe = 0
    for i in range(li, re + 1):
        zwischensumme += A[i]
        max_summe = max(max_summe, zwischensumme)
    return max_summe


a = [1, 2, 3, 4, -5]
filename = input("Please enter filename: ")

with open(filename) as f:
    lines = f.readlines()
    for line in lines:
        integer = int(line.replace("\n", ""))
        a.append(integer)

start = time.time()
ergebnis = maxTeilsummerek(a, 0, len(a) - 1)
end = time.time()
print("Das Maximum der Teilsumme des Arrays ist", ergebnis)

runtime = end - start
runtimeAsString = ("%.18f" % runtime)
print("Runtime: " + runtimeAsString + "s")