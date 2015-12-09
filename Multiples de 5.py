#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Hugo Pezzo
print("Tous les nombres doivent être positifs")
a = int(input("Entrez un nombre a : "))
b = int(input("Entrez un nombre b : "))
z = 0
if a>b:
	z = a
	a = b
	b = z
x = a
y = 0
while x<=b:
	if (x%5 == 0):
		y = y+x
	x = x+1
print("La somme des multiples de 5 dans cet intervalle est de",y,)
