# argmax function
def argmax(vector):
	index, value = 0, vector[0]
	for i,v in enumerate(vector):
		if v > value:
			index, value = i,v
	return index

# define vector
vector = [0.4, 0.5, 0.1,1]
# get argmax
result = argmax(vector)
print('arg max of %s: %d' % (vector, result))