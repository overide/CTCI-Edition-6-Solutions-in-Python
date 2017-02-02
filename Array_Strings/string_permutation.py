# Cracking the Coding interview Problems
# find all permutation of the string

def permutation(remaining,prefix=""):
	remaining = list(remaining)
	if(len(remaining)==1):
		return list(remaining)
	else:
		permutations = []
		for i,_ in enumerate(remaining):
			tmp_set = []
			prefix = remaining[i]
			rem = remaining[0:i]+remaining[i+1:]
			tmp_per = permutation(rem,prefix)
			for e in tmp_per:
				tmp_set.append(prefix+e)
			permutations+=tmp_set
		return permutations