import gPair
from random import randint
from math import fmod 

p = gPair.p
g = gPair.g

publicKey = []
masterKey = []

# RICORDA
# Gli attributi vengono contati da 0 e non da 1!

def setupKnU(n):
	attributi = range(n+1)
	for i in attributi:
		tmp = 0
		while True:
			tmp = randint(1,p-1)
			if tmp not in masterKey: break

		masterKey.append(tmp)
	for x in masterKey:
		publicKey.append(int(fmod(g ** x , p)))
	return attributi

def encrypto(messaggio, attr):
	s = randint(1,p-1)
	messcrypt = int(fmod(messaggio * ( publicKey[-1]**s ),p))
	attricry = []
	for att in attr:
		attricry.append( int(fmod( publicKey[attributi.index(att)]**s,p ) ))
	return (attr,messcrypt,attricry)



attributi = setupKnU(4)