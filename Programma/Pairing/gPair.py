# Variabili globali per il sistema
# p deve esser primo
# g un generatore del gruppo ciclico Cp

import math

# p = 31
# g = 3

p = 101
g = 2

potenze = []

def inizializza():
	for i in range(p-1):
		potenze.append(math.fmod(g**i , p))
	return potenze

def e(a,b):
	return math.fmod(g**(int(math.fmod(potenze.index(a)*potenze.index(b),(p-1) ))),p)

def inverse(n):
	while n<0:
		n = int(math.fmod(n+p , p))
	return int(math.fmod(g**(p-1 - potenze.index(n)),p))

def powerEff(a,b):
	return int(math.fmod(g**(int(math.fmod(potenze.index(a)*b,(p-1) ))),p))

potenze = inizializza()

print [n for n in range(1,p) if set(range(1,p)).issubset(set([powerEff(x,n) for x in potenze]))]