from random import choice

class Node:
	def __init__(self, n_type, value, children=None, leaf=None):
		self.type = n_type
		self.value = value
		if children:
			self.children = children
		else:
			self.children = [ ]

		self.leaf = leaf
	def __repr__(self, level=0):
		ret = "\t"*level+repr(self.value)+"\n"
		for child in self.children:
			ret += child.__repr__(level+1)
		return ret


def printYield(root, reqpos, type):
    # Stack to store all the nodes  
    # of tree  
    s1 = []  
  
    # Stack to store all the 
    # leaf nodes  
    s2 = []  
  
    # Push the root node  
    s1.append(root)  
    n=0
    while len(s1) != 0:  
        curr = s1.pop()  
  
        # If current node has a left child  
        # push it onto the first stack  
        for child in curr.children:
        	s1.append(child)
  
        if curr.leaf:
            n+=1
            if type == "remove" and n not in reqpos:
                s2.append(curr)

            if type == "add":
                s2.append(curr)
                if n in reqpos:
                    temp = Node("dummy", "errnode", leaf = 1)
                    s2.append(temp)
            if type == "replace":
                if n in reqpos:
                    temp = Node("dummy", "@@@", leaf = 1)
                    s2.append(temp)
                else:
                    s2.append(curr)

    # Print all the leaf nodes  
    level = 0
    while len(s2) != 0:
    	val = s2.pop()
    	print("\t"*level + val.value, end = " ")

    	if val == colon:
    		print("")
    		level += 1

    print("\n------------------------------\n")

def getPgmLen(root):
    s1 = []  
    s2 = []  
    s1.append(root)
    while len(s1) != 0:  
        curr = s1.pop()    
        for child in curr.children:
            s1.append(child)
  
        if curr.leaf:
            s2.append(curr)  

    return len(s2)

ret = Node("keyword","return", leaf = 1)

zero = Node("number","0", leaf = 1)
block = Node("block", "block", [ret, zero], leaf = 0)
openp = Node("symbol","(", leaf = 1)
closep = Node("symbol",")", leaf = 1)
colon = Node("symbol",":", leaf = 1)
def_k = Node("keyword","def", leaf = 1)
fname = Node("identifier", "fname", leaf = 1)
function = Node("function", "function", [def_k, fname, openp, closep, colon, block], leaf = 0)

printYield(function, [0], "remove")
pgmLen = getPgmLen(function)
print(function.__repr__())


#### now we will try to introduce errors in the above syntax tree
print("")
# printYield(function, [7])
pgms =  2
print("Removal of nodes: ")
positions = [i for i in range(1,pgmLen)]
for n_errors in range(1,4):
    print("Programs with "+str(n_errors)+" errors")
    for i in range(0,pgms):
        reqpos = []    
        for j in range(0,n_errors):
            c = choice(positions)
            reqpos.append(c)
            positions.remove(c)
        positions = [i for i in range(1,pgmLen)]
        printYield(function, reqpos, "remove")
        print("")
    
print("Addition of nodes: ")
positions = [i for i in range(1,pgmLen)]
for n_errors in range(1,4):
    print("Programs with "+str(n_errors)+" errors")
    for i in range(0,pgms):
        reqpos = []    
        for j in range(0,n_errors):
            c = choice(positions)
            reqpos.append(c)
            positions.remove(c)

        positions = [i for i in range(1,pgmLen)]
        printYield(function, reqpos, "add")
        print("")

print("Replacing of nodes: ")
positions = [i for i in range(1,pgmLen)]
for n_errors in range(1,4):
    print("Programs with "+str(n_errors)+" errors")
    for i in range(0,pgms):
        reqpos = []    
        for j in range(0,n_errors):
            c = choice(positions)
            reqpos.append(c)
            positions.remove(c)

        positions = [i for i in range(1,pgmLen)]
        printYield(function, reqpos, "replace")
        print("")

