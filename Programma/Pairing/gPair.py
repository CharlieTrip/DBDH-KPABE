# Variabili globali per il sistema
# p deve esser primo
# g un generatore del gruppo ciclico Cp

import math

p = 101
g = 2
g1 = 3

potenze = []

def potenze():
	return [int(math.fmod(g*n,p)) for n in range(p)]

def e(a,b):
	return int(math.fmod( (potenze.index(a)*potenze.index(b))*g1 ,p))

def pro(a,b):
	return int(math.fmod( (a+b) ,p))

def pot(a,b):
	return int(math.fmod( (a*b) ,p))

def inverse(n):
	return p-n

def radice(a,n):
	return pot(a, int(math.fmod(( int(math.fmod(extendedEuclideanAlgorithm(n,p)[0] , p))*extendedEuclideanAlgorithm(n,p)[2] + p),p)))


def extendedEuclideanAlgorithm(a, b):
   if abs(b) > abs(a):
      (x,y,d) = extendedEuclideanAlgorithm(b, a)
      return (y,x,d)
   if abs(b) == 0:
      return (1, 0, a)
   x1, x2, y1, y2 = 0, 1, 1, 0
   while abs(b) > 0:
      q, r = divmod(a,b)
      x = x2 - q*x1
      y = y2 - q*y1
      a, b, x2, x1, y2, y1 = b, r, x1, x, y1, y
   return (x2, y2, a)

potenze = potenze()