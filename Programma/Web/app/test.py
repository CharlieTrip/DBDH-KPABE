from cripto import Crypto
from decrypto import deCrypto
from tree import tree
import flask

cry = Crypto(5)


alb1 = tree(2,[0,1,2],[
	tree(1,[0],[]),
	tree(1,[2],[])
	])

alb2 = tree(2,[0,1,2,3], [
	tree(1,[0,1,2],[
		tree(1,[0],[]),tree(1,[2],[])]
		),
	tree(1,[3],[]) 
	])

pk1 = cry.keygenerator.keygen(alb1)
pk2 = cry.keygenerator.keygen(alb2)

decry1 = deCrypto(alb1,pk1)
decry2 = deCrypto(alb2,pk2)

def chiavePubblica():
	tmp = "PK :"
	for x in cry.publicKey:
		tmp = "{} {}".format(tmp,x)
	return tmp

def encrypt(mess,att):
	E = cry.encrypto(mess,att)
	return E[1]

def chiaviPrivate1():
	pk = pk1
	tmp = "Chiavi Private :"
	for x in pk:
		tmp = "{} {}->{}".format(tmp,x[0],x[1])
	return tmp

def chiaviPrivate2():
	pk = pk2
	tmp = "Chiavi Private :"
	for x in pk:
		tmp = "{} {}->{}".format(tmp,x[0],x[1])
	return tmp

def decrypt1(E,pk):
	return decry1.decifra(E,pk)

def decrypt2(E,pk):
	return decry2.decifra(E,pk)

