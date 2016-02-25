#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Hugo Pezzo
print ("Debut du programme:")
P= input("Entrez votre phrase : ")
tableau=P.split()
i=0
k=0
for a in tableau:
	i= len(a)
	if i > k:
	  k=i
	  V=a
print ("Le mot le plus long est:")
print (V)
print ("de")
print (k)
print ("caractères.")
print ("Fin du programme.")
