
<br/> class Node : 
<br/> 	def __init__ ( self , data  <span style="color:red">)</span> 
<br/> 		self . data  <span style="color:red">=</span>  <span style="color:red">=</span> data 
<br/> 		self . left  <span style="color:red">=</span> None 
<br/> 		self . right  <span style="color:red">=</span>  <span style="color:red">=</span> None 
<br/> def size node )  <span style="color:red">(</span> : 
<br/> 	if node is None : 
<br/> 		return 0 
<br/> 	else : 
<br/> 		return ( size ( node . left ) + 1 + size ( node . right ) ) 
<br/> root  <span style="color:red">=</span> Node ( 1 ) 
<br/> root . left = Node ( 2 ) 
<br/> root . right = Node ( 3 ) 
<br/> root . left  <span style="color:red">.</span>  <span style="color:red">.</span> left Node ( 4 )  <span style="color:red">.</span> 
<br/> root . left . right = Node ( 5 ) 
<br/> print "Size of the tree is %d" % ( size ( root ) ) 
<br/>  <span style="color:red">.</span> 
<br/> 