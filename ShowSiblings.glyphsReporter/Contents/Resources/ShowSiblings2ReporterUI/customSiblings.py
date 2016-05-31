# encoding: utf-8
from collections import OrderedDict

"""
def func():
	Latin__Siblings__ = []
	Latin__Siblings__.append("1")
	Cyrillic__Siblings__ = []
	Cyrillic__Siblings__.append("1")
	Cyrillic__Siblings__.append("2")
	Greek__Siblings__ = []
	Greek__Siblings__.append("1")
	Phantasy__Siblings__ = []
	Phantasy__Siblings__.append("4")	
	
	for var in func.__code__.co_varnames:
		print(var, locals()[var])	
	
func()
"""

def availableScripts():
	scripts = OrderedDict()
	
	
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	# + + + START: C U S T O M I Z A B L E + + + 
	#
	Latin__Siblings__ = []
	#### maybe in special function
	### TAKE CARE TO HAVE NO DOUBLE ENTRIES
	### !!
	#************************************
	########
	Latin__Siblings__.append( ("c", "e", "o") ) # "eth"
	Latin__Siblings__.append( ("b", "p") )
	########

	Latin__Siblings__.append( ("i", "j") )
	Latin__Siblings__.append( ("t", "f")  )
	Latin__Siblings__.append( ("k", "x") )
	Latin__Siblings__.append( ("v", "y") )
	Latin__Siblings__.append( ("ae", "oe") )
	
	Latin__Siblings__.append( ("B", "D", "P", "R") )
	Latin__Siblings__.append( ("C", "G", "O", "Q") )
	Latin__Siblings__.append( ("H", "U", "N") )
	Latin__Siblings__.append( ("K", "V", "X", "Y") )



	Cyrillic__Siblings__ = []
	### TAKE CARE TO HAVE NO DOUBLE ENTRIES
	### !!
	#************************************		
	Cyrillic__Siblings__.append( ("o-cy", "be-cy", "fita-cy", "obarred-cy") )
	Cyrillic__Siblings__.append( ("ef-cy", "sha-cy", "iu-cy") ) # "zhe-cy"
	Cyrillic__Siblings__.append( ("el-cy", "de-cy", "lje-cy") )
	Cyrillic__Siblings__.append( ("ka-cy", "k") )
	Cyrillic__Siblings__.append( ("ve-cy", "softsign-cy", "hardsign-cy") )
	# Cyrillic__Siblings__.append( ("ge-cy", "gheupturn-cy", "pe-cy") )
	Cyrillic__Siblings__.append( ("en-cy", "ii-cy", "pe-cy", "tse-cy") ) #"ge-cy", 
	Cyrillic__Siblings__.append( ("ia-cy", "zhe-cy", "x") )
	Cyrillic__Siblings__.append( ("e-cy", "ereversed-cy", "c", "o") )
	Cyrillic__Siblings__.append( ("ze-cy", "three") )
	
	# Cyrillic__Siblings__.append( ("Ii-cy", "H", "N") ) #, "Nje-cy"
	Cyrillic__Siblings__.append( ("Ef-cy", "Sha-cy", "Iu-cy") ) # "Zhe-cy"
	Cyrillic__Siblings__.append( ("El-cy", "De-cy", "Lje-cy") )
	# Cyrillic__Siblings__.append( ("Ge-cy", "Gheupturn-cy", "Pe-cy") )
	Cyrillic__Siblings__.append( ("En-cy", "Ii-cy", "Pe-cy", "Tse-cy") ) # "Ge-cy", 
	# Cyrillic__Siblings__.append( ("Be-cy", "Ve-cy", "Ge-cy", "Gheupturn-cy", "Softsign-cy") )
	Cyrillic__Siblings__.append( ("Be-cy", "Ve-cy", "Softsign-cy") ) # "Ge-cy", "Gheupturn-cy",
	Cyrillic__Siblings__.append( ("Ze-cy", "B", "three") )
	Cyrillic__Siblings__.append( ("Ka-cy", "K", "X") )
	Cyrillic__Siblings__.append( ("E-cy", "Ereversed-cy", "C", "O") )
	Cyrillic__Siblings__.append( ("Obarred-cy", "O") )
	Cyrillic__Siblings__.append( ("Ia-cy", "Zhe-cy", "X") )
	Cyrillic__Siblings__.append( ("Tshe-cy", "Dje-cy") )
	Cyrillic__Siblings__.append( ("Hardsign-cy", "Yeru-cy") )  # NOT REALLY



	Greek__Siblings__ = []
	### TAKE CARE TO HAVE NO DOUBLE ENTRIES
	### !!
	#************************************
	Greek__Siblings__.append( ("kappa", "k") )
	Greek__Siblings__.append( ("mu", "u") )
	Greek__Siblings__.append( ("nu", "gamma", "v", "y") )
	Greek__Siblings__.append( ("zeta", "xi", "sigmafinal", "epsilon", "c") )
	#Greek__Siblings__.append( ("beta", "germandbls") )
	Greek__Siblings__.append( ("beta", "germandbls", "rho", "p") ) #"sigma"
	Greek__Siblings__.append( ("iota", "tau", "i") )
	Greek__Siblings__.append( ("upsilon", "sigma", "delta", "theta", "omicron") ) # u
	Greek__Siblings__.append( ("chi", "x") )
	Greek__Siblings__.append( ("psi", "phi", "omega") )

	Greek__Siblings__.append( ("Delta", "Lambda", "A") )
	Greek__Siblings__.append( ("Xi", "Sigma", "E", "Z") )
	Greek__Siblings__.append( ("Omega", "O") )
	Greek__Siblings__.append( ("Phi", "Psi", "U") )
	Greek__Siblings__.append( ("Theta", "Omicron") )
	Greek__Siblings__.append( ("Pi", "Eta") )

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

	# Kanji__Siblings__ = []
	### TAKE CARE TO HAVE NO DOUBLE ENTRIES
	### !!
	#************************************		
	# Kanji__Siblings__.append( ("o-cy", "be-cy", "fita-cy", "obarred-cy") )
	# Kanji__Siblings__.append( ("ef-cy", "sha-cy", "iu-cy") )

	#
	# + + + END: C U S T O M I Z A B L E + + + 
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++


	# for vars, value in OrderedDict(locals()).items():
	# 	if vars.endswith("__Siblings__"):
	# 		scripts[vars] = value
	# return scripts

	# Hangul__Siblings__ = []
	# Hangul__Siblings__.append( ("Theta", "Eta", "Omicron") )

	### DO NOT TOUCH:
	for var in availableScripts.__code__.co_varnames:
		s = locals()[var]
		if var.endswith("__Siblings__"):
			if type(s) == list:
				scripts[var] = locals()[var]
	return scripts



