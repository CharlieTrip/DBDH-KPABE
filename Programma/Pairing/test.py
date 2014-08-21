from cripto import Crypto
from decrypto import deCrypto
from tree import tree

cry = Crypto(3)

# alb1 = tree(2,[0,1,2,3], [
# 	tree(1,[0,1,2],[
# 		tree(1,[0],[]),tree(1,[2],[])]
# 		),
# 	tree(1,[3],[]) 
# 	])

alb1 = tree(2,[0,1,2],[
	tree(1,[0],[]),
	tree(1,[2],[])
	])

att = [0,2]
mess = 1



print "Public Key : {}".format(cry.publicKey)
print "Master Key : {}".format(cry.masterKey)
E = cry.encrypto(mess,att)

print "Ciphertext : {}".format(E)

privatekey1 = cry.keygenerator.keygen(alb1)

print "Private Key {} \n for {} ".format(privatekey1,alb1)

decry = deCrypto(alb1,privatekey1)


print "Mess: {}".format(decry.decifra(E,privatekey1))