#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Hugo Pezzo
print("Pouvez-vous conduire une voiture?")
a= int(input("Entrez votre âge :"))
#On demande l'age de la personne
p= (input("Entrez votre prénom :"))
if a < 18:
	print("Bonjour", p, "je suis désolé mais vous ne pouvez pas conduire une voiture")
else:
	print("Bonjour", p, "vous pouvez conduire une voiture! Félicitations")
