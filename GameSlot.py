




def matchWord(keyboard,v,word,n, dir=None):
	k1 = False
	if len(word) > 0 :
		if v[0]-1 >=0 and word[0] == keyboard[v[0]-1][v[1]] and  (dir=="L" or dir==None):
			k1 |= matchWord(keyboard,(v[0]-1,v[1]),word[1:],n,"L")
		if v[0]+1 <= n and word[0] == keyboard[v[0]+1][v[1]] and (dir=="R" or dir==None):
			k1 |= matchWord(keyboard,(v[0]+1,v[1]),word[1:],n,"R")
		if v[1]-1 >=0 and word[0] == keyboard[v[0]][v[1]-1] and (dir=="U" or dir==None):
			k1 |= matchWord(keyboard,(v[0],v[1]-1),word[1:],n,"U")
		if v[1]+1 <= n and word[0] == keyboard[v[0]][v[1]+1] and (dir=="D" or dir==None):
			k1 |= matchWord(keyboard,(v[0],v[1]+1),word[1:],n,"D")
		if v[0]-1 >=0 and v[1]-1 >=0 and word[0] == keyboard[v[0]-1][v[1]-1] and (dir=="NW" or dir==None):
			k1 |= matchWord(keyboard,(v[0]-1,v[1]-1),word[1:],n,"NW")
		if v[0]+1 <= n and v[1]-1>=0 and word[0] == keyboard[v[0]+1][v[1]-1] and (dir=="NE" or dir==None):
			k1 |= matchWord(keyboard,(v[0]+1,v[1]-1),word[1:],n,"NE")
		if v[1]+1 <=n and v[0]+1<=n and word[0] == keyboard[v[0]+1][v[1]+1] and (dir=="SE" or dir==None):
			k1 |= matchWord(keyboard,(v[0]+1,v[1]+1),word[1:],n,"SE")
		if v[1]+1 <= n and v[0]-1 >=0  and word[0] == keyboard[v[0]-1][v[1]+1] and (dir=="SW" or dir==None):
			k1 |= matchWord(keyboard,(v[0]-1,v[1]+1),word[1:],n,"SW")
		return False | k1
	else:
		return True

def findword(keyboard,word):
	temp = []
	for i in xrange(0,len(keyboard)):
		for j in xrange(0,len(keyboard[i])):
			# import pdb;pdb.set_trace()
			if keyboard[i][j] == word[0]:
				temp.append((i,j))

	if len(temp) > 0:
		ret =  False
		for v in temp:
			ret |= matchWord(keyboard,v,word[1:],len(keyboard)-1)
		return ret
	else:
		return False

# army
# raid
# ptre
# team



if __name__ == "__main__":
	keyboard = [['a','r','m','y'],['r','a','i','d'],['p','t','r','e'],['t','e','a','m']]
	word = "pot"
	word = "map"
	word = "ate"
	word = "army"
	word = "dre"
	print findword(keyboard,word)