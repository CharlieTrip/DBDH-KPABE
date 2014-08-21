import gPair
from random import randint
from math import fmod 
from keygen import KeyGene

# RICORDA
# Gli attributi vengono contati da 0 e non da 1!
class Crypto:


	p = gPair.p
	g = gPair.g	
	publicKey = []
	masterKey = []

	def __init__(self,n):


		self.attributi = range(n+1)
		for i in self.attributi:
			tmp = 0
			while True:
				tmp = randint(1,self.p-1)
				if tmp not in self.masterKey: break

			self.masterKey.append(tmp)
		for x in self.masterKey:
			self.publicKey.append(int(fmod(self.g ** x , self.p)))
		self.keygenerator = KeyGene(self.masterKey)
	
	def encrypto(self,messaggio, attr):
		s = randint(1,self.p-1)
		
		messcrypt = int(fmod(messaggio * ( int(fmod(self.publicKey[-1]**s,self.p)) ),self.p))
		attricry = []
		for att in attr:
			attricry.append( int(fmod( self.publicKey[self.attributi.index(att)]**s,self.p ) ))
		return (attr,messcrypt,attricry)
