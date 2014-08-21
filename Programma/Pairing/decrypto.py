import gPair
from math import fmod


class deCrypto:
	def __init__(self,albero,privateKey):
		self.albero = albero
		self.privateKey = privateKey

	def lagrangeCoeff(i,S,val):
		return int(fmod(reduce((lambda x,y:x*y),[ int(fmod( (j - val) * gPair.inverse(j - i) ,gPair.p) ) for j in S if j!= i],1),gPair.p))

	# def decifraFiglio(E,D):
	# 	if x.attributi in E[0]:
	# 		return gPair.e()

	# def decifraNodo(E,D):
	# 	if x.children == []
