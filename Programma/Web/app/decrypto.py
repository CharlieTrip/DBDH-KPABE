import gPair
from math import fmod


class deCrypto:
	def __init__(self,albero,privateKey):
		self.albero = albero
		self.privateKey = privateKey

	def lagrangeCoeff(self,i,S,val):
		# return (coef sopra) , (coef sotto) <- sotto comporta una radice nel conto
		return int(fmod(reduce((lambda x,y:x*y),[ int(fmod( (j - val), gPair.p)) for j in S if j!= i],1),gPair.p)) , int(reduce((lambda x,y:x*y),[ j-i  for j in S if j!= i],1))

	def decifraFoglia(self,E,D,x):
		if x.attribute[0] in E[0]:
			return int(gPair.e([y for xx,y in self.privateKey if xx==x.attribute[0] ][0],E[2][E[0].index(x.attribute[0])]))
		else: return -1

	def decifraNodo(self,E,D,x):
		if x.children == []:
			return self.decifraFoglia(E,D,x)
		else:
			fz = [( x.children.index(z)+1 ,self.decifraNodo(E,D,z)) for z in x.children ]
			sxcompleto = [(xx,y) for xx,y in fz if y != -1]
			if len(sxcompleto) < x.threshold:
				return -1
			else:
				sx = sxcompleto[:x.threshold]
				sprimex = [xx for xx,y in sx]
				return int(fmod(reduce((lambda x,y: x + y),[ gPair.pot(gPair.radice(y,self.lagrangeCoeff(x,sprimex,0)[1]),self.lagrangeCoeff(x,sprimex,0)[0])  for x,y in sx],0) + gPair.p  , gPair.p))


	def decifra(self,E,D):
		if self.albero.accettaAlbero(E[0]):	
			return gPair.pro( E[1] , gPair.inverse(self.decifraNodo(E,D,self.albero)))
		else:
			return -1