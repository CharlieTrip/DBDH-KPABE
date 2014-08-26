import gPair
from math import fmod


class deCrypto:
	def __init__(self,albero,privateKey):
		self.albero = albero
		self.privateKey = privateKey

	def lagrangeCoeff(self,i,S,val):
		return int(fmod(reduce((lambda x,y:x*y),[ int(fmod( (j - val) * gPair.inverse(j - i) ,gPair.p) ) for j in S if j!= i],1),gPair.p))

	def decifraFoglia(self,E,D,x):
		if x.attribute[0] in E[0]:
			print "Figlio : c {} h {}".format([y for xx,y in self.privateKey if xx==x.attribute[0] ],E[2][E[0].index(x.attribute[0])] )
			return int(gPair.e([y for xx,y in self.privateKey if xx==x.attribute[0] ][0],E[2][E[0].index(x.attribute[0])]))
		else: return -1

	def decifraNodo(self,E,D,x):
		if x.children == []:
			return self.decifraFoglia(E,D,x)
		else:
			fz = [( x.children.index(z)+1 ,self.decifraNodo(E,D,z)) for z in x.children ]
			sxcompleto = [(xx,y) for xx,y in fz if y != -1]
			if len(sxcompleto) < x.threshold:
				return 1
			else:
				sx = sxcompleto[:x.threshold]
				sprimex = [xx for xx,y in sx]
				print "{} th".format(x.threshold)
				print "{} insieme, {} indici, {} potenze, {} lagrange".format(sx,sprimex, [gPair.prodo(y,self.lagrangeCoeff(x,sprimex,0)) for x,y in sx], [self.lagrangeCoeff(x,sprimex,0) for x,y in sx])
				print "{} prodotto".format(int(fmod(reduce((lambda x,y:x*y), [int(fmod( y**self.lagrangeCoeff(x,sprimex,0) , gPair.p)) for x,y in sx] ,1),gPair.p)))
				return int(fmod(reduce((lambda x,y:x*y), [int(fmod( y*self.lagrangeCoeff(x,sprimex,0) , gPair.p)) for x,y in sx] ,1),gPair.p))

	def decifra(self,E,D):
		if self.albero.accettaAlbero(E[0]):	
			return int(fmod( E[1]  * gPair.inverse2(self.decifraNodo(E,D,self.albero)),gPair.p))
		else:
			return -1