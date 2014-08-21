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
		key =[(x[0] , int(fmod( gPair.g**(int(fmod(y * gPair.inverse( self.masterKey[x[0]-1] ),(gPair.p - 1) ))) , gPair.p)) ) for x,y in foglie ]
		return key
