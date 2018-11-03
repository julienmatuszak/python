def split_sentence(a):
	b=a.split()
	print(b)
	return(b)

def rearrange_way_back(a):
	return(a[::-1])

def join_sentence(a):
	b = " ".join(a)
	return(b)

print(join_sentence(rearrange_way_back(split_sentence("VIE DE MERDE"))))
#print(join_sentence(rearrange_way_back(split_sentence()))