from math import fmod
from random import randint
from tree import tree , keyTree
import gPair

class KeyGene:
	masterKey = []

	def __init__(self,masterKey):
		self.masterKey = masterKey

	def keygen(self,albero):
		alberochiavi = keyTree()
		alberochiavi.generaFunzioni(albero, self.masterKey[-1])
		foglie = alberochiavi.estraiFoglie()
		print foglie
		key =[(x[0] ,gPair.pot(gPair.radice(gPair.g , self.masterKey[x[0]])  , y)) for x,y in foglie ]
		return key
