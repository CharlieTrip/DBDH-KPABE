# Variabili globali per il sistema
# p deve esser primo
# g un generatore del gruppo ciclico Cp

import math

p = 31
g = 2
g1 = 3

potenze = []

def potenze():
	return [int(math.fmod(g1*n,p)) for n in range(p)]
def e(a,b):
	return int(math.fmod( (potenze.index(a)*potenze.index(b))*g ,p))

def prodo(a,b):
	return int(math.fmod( (a+b) ,p))

def inverse2(n):
	return p-n

def inverse(n):
	return p-n

potenze = potenze()