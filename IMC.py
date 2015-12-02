#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Hugo Pezzo
print("Calcul de l'IMC")
n=input("Entrez votre nom :")
m=float(input("Entrez votre taille en mètres :"))
kg=int(input("Entrez votre poids en Kg :"))
IMC=(kg/(m*m))
if IMC<16.5:
	print ("IMC =",IMC,)
	print ("Desole", n, "vous etes en denutrition")
if IMC>=16.5 and IMC<=18.5:
	print ("IMC =",IMC,)
	print ("vous etes maigre", n,", il faut manger plus!")
if IMC>=18.5 and IMC<=25:
	print ("IMC =",IMC,)
	print ("Bravo", n,", Vous avez une corpulence normale!")
if IMC>=25 and IMC<=30:
	print ("IMC =",IMC,)
	print ("Faites attention à votre ligne", n,", vous etes en surpoids.")
if IMC>=30 and IMC<=35:
	print ("IMC =",IMC,)
	print ("Attention", n,", vous etes en obesite moderee.")
if IMC>=35 and IMC<=40:
	print ("IMC =",IMC,)
	print ("faites attation", n,", vous etes en obesite severe!")
if IMC>40:
	print ("IMC =",IMC,)
	print ("faites tres attention", n,", Vous etes en obesite Morbide!!")

