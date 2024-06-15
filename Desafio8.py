import sympy as sp
M0 = sp.Symbol('M0')
Mw = sp.Symbol('Mw')

f1 = 10**(3/2*(Mw+10.7))

Mw1 = 9.5
Mw2 = 8.7

cM01 = f1.evalf(subs = {Mw: Mw1})
cM02 = f1.evalf(subs = {Mw: Mw2})

eM01 = 0.001
eM02 = 0.001

f2 = (2/3)*sp.log(M0,10)-10.7

df2 = sp.diff(f2, M0)

ef1 = df2.evalf(subs = {M0: cM01})
ef2 = df2.evalf(subs = {M0: cM02})

prop1 = abs(ef1)*eM01
prop2 = abs(ef2)*eM02

Chile = round(f2.evalf(subs = {M0: cM01}),1)
Alaska = round(f2.evalf(subs = {M0: cM02}),1)

print("Chile: ", Chile," +- ", prop1)
print("Alaska: ", Alaska," +- ", prop2)
print("El terremoto de Chile libero ", round(cM01/cM02, 2), " veces más energía que el terremoto de Alaska.")