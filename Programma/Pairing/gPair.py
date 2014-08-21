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
	return math.fmod(g**(potenze.index(a)*potenze.index(b)),p)

def inverse(n):
	while n<0:
		n = int(math.fmod(n+p , p))
	return int(math.fmod(g**(p-1 - potenze.index(n)),p))

potenze = inizializza()
