class tree(object):
	def __init__ (self,threshold,attribute,children = []):
		
		if threshold <= len(children):
			self.threshold = threshold
		else:
			self.threshold = len(children)
		self.attribute = attribute
		self.children = children

	def accettaAlbero(self,insieme):
		print "{} in {}".format(self.attribute , insieme)
		if self.children == [] :
			if set(self.attribute).issubset(set(insieme)):
				return 1
			else:
				return 0
		else:
			somma = 0
			for child in self.children:
				somma = somma + child.accettaAlbero(insieme)
			if self.threshold <= somma:
				return 1
			else:
				return 0

	def stringato(self):
		print "th {},att {},ch {} -".format(self.threshold,self.attribute,self.children)


# alb = tree(2,[1,2,3,4], [
# 	tree(2,[1,2,3],[
# 		tree(1,[1],[]),tree(1,[2,3],[])]
# 		),
# 	tree(1,[3,4],[]) 
# 	])



class keytree(object):
	def __init__ (self):
		self.children = []

	def generaFunzioni(self,albero,valore):
		self.grado = int(albero.threshold) - 1
		self.attributi = alberi.attribute

		if self.grado != 0:
			self.funzione = lambda x : (x**self.grado ) + valore
		else:
			self.funzione = lambda x : valore
		for child in albero.children:
			kt = keytree()
			self.children.append(kt)
			kt.generaFunzioni(child,self.funzione(albero.children.index(child)+1))
