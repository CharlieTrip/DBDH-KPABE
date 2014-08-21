class tree(object):
	def __init__ (self,threshold,attribute,children):
		
		if threshold <= len(children):
			self.threshold = threshold
		elif len(children) > 0:
			self.threshold = len(children)
		else:
			self.threshold = 1
		self.attribute = attribute
		self.children = children

	def accettaAlbero(self,insieme):
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


class keyTree(object):
	def __init__ (self):
		self.children = []

	def generaFunzioni(self,albero,valore):
		self.grado = int(albero.threshold) - 1
		self.attributi = albero.attribute

		if self.grado > 0:
			self.funzione = lambda x : (x**self.grado ) + valore
		else:
			self.funzione = lambda x : valore
		for child in albero.children:
			kt = keyTree()
			self.children.append(kt)
			kt.generaFunzioni(child,self.funzione(albero.children.index(child)+1))
	
	def estraiFoglie(self):
		if self.children == []:
			return [(self.attributi , self.funzione(0))]
		else:
			dic = []
			for child in self.children:
				dic.extend(child.estraiFoglie())
			return dic
