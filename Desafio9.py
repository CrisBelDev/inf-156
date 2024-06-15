import math
x = int(input("Ingrese un numero x: "))
sum = y = i = 0
test = 1
print("x: ",x,"\n\t i\t term\t sum")
while sum != test:
    test = sum
    y = x**i/math.factorial(i)
    sum =  sum + y
    if i < 6 or i > 54:
        print("\t", i, "\t", y, "\t", sum)
    i+=1
print("Valor exacto: ", math.exp(x))