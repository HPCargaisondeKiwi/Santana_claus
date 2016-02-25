#Consigne : Ecrivez un script capable d'afficher la liste de tous les jours d'une année qui commence un lundi. #
#Votre script utilisera lui-même trois listes : une des jours, une des mois et une des nombres.#

print ("Voila le calendrier de l'année : ") #affiche le message#
NomJour=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]#tableau 1 : nom des jours#
NomMois=["janvier","février","mars","avril","mai","juin","juillet","aout","septembre","novembre","décembre"]#tableau 2 : nom des mois#
FinMois=[31,28,30,31,30,31,31,30,31,30,31]#tableau 3 : nombre de jours dans un mois#
NumeroJour=1
IndiceDuNomDuJour=0
for Mois in NomMois:
	while NumeroJour<=FinMois:
		print (NomJour[IndiceDuNomDuJour])
		print (NumeroJour)
		print (Mois)
		NumeroJour=NumeroJour+1
		if IndiceDuNomDuJour>6 :
		    IndiceDuNomDuJour=0
		if IndiceDuNomDuJour<=6 :
		    IndiceDuNomDuJour=IndiceDuNomDuJour+1
	FinMois=FinMois+1
