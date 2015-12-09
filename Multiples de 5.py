#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Hugo Pezzo
a = int(input("Entrez un nombre a : "))
b = int(input("Entrez un nombre b : "))
z = 0
if a>b:					#Si les nombres sont tels que a>b, on les échangent
	z = a
	a = b
	b = z
x = a
y = 0
while x<=b:				#Si le modulo donne 0, cela veut dire que le nombre est un multiple de 5
	if (x%5 == 0):
		y = y+x
	x = x+1
print("La somme des multiples de 5 dans cet intervalle est de",y,)
