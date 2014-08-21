from cripto import Crypto
from decrypto import deCrypto
from tree import tree

cry = Crypto(4)

alb1 = tree(2,[0,1,2,3], [
	tree(2,[0,1,2],[
		tree(1,[0],[]),tree(1,[2],[])]
		),
	tree(1,[3],[]) 
	])

att = [0,2]
mess = 23

print "Public Key : {}".format(cry.publicKey)

E = cry.encrypto(mess,att)

print "Ciphertext : {}".format(E)

privatekey1 = cry.keygenerator.keygen(alb1)

print "Private Key {} \n for {} ".format(privatekey1,alb1)

decry = deCrypto(alb1,privatekey1)

