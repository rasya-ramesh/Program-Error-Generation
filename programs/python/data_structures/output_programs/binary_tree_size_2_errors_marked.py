
<br/> class Node : 
<br/> 	def __init__ ( self , data ) : 
<br/> 		self . data = data 
<br/> 		self . left = None 
<br/> 		self . right = None 
<br/> def size ( node )  <span style="color:red">:</span> 
<br/> 	if node is None : 
<br/> 		return 0 
<br/> 	else : 
<br/> 		return size ( node . left ) + 1 + size ( node . right ) )  <span style="color:red">^</span> 
<br/> root Node  <span style="color:red">(</span>  <span style="color:red">(</span> 1 )  <span style="color:red">`</span> 
<br/> root . left = Node ( 2 ) 
<br/> root . right = Node  <span style="color:red">&</span> ( 3 ) 
<br/> root . left . left = Node ( 4  <span style="color:red">@</span> ) 
<br/> root . left . right  <span style="color:red">=</span> Node 5 )  <span style="color:red">[</span> 
<br/> print "Size of the tree is %d" % ( size ( root  <span style="color:red">)</span> ) 
<br/> 
<br/> 