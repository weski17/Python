def rekursion(i , x=2):

    if i == 0 :
        return 1
    elif i < 0 :
        return (1/x) * (rekursion(i+1,x))
    else:
        return x * rekursion(i-1,x)



print("Geben Sie den Exponent ein ")
power_1 = int(input())
print("Möchten Sie eine Zahl eingeben ")
print("j = Ja ")
print("n = nein")
cheak = input()

if cheak == "n" :
    print("Das Potenzwert = ",rekursion(power_1, x =2 ))
else:
    print("Geben Sie den Basis ein ")
    basis = int(input())
    print("Das Potenzwert = ",rekursion(power_1, basis))