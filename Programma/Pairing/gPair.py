# Variabili globali per il sistema
# p deve esser primo
# g un generatore del gruppo ciclico Cp

import math

p = 31
g = 3
potenze = []

def inizializza():
	for i in range(p-1):
		potenze.append(math.fmod(g**i , p))
	return potenze

def e(a,b):
	return math.fmod(g**(potenze.index(a)*potenze.index(b)),31)

potenze = inizializza()