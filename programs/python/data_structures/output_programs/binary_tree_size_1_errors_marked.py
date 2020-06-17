
<br/> class Node : 
<br/> 	def __init__ ( self  <span style="color:red">,</span> data ) : 
<br/> 		self . data = data 
<br/> 		self . left  <span style="color:red">=</span>  <span style="color:red">=</span> None 
<br/> 		self . right = None 
<br/> def size ( node )  <span style="color:red">:</span> 
<br/> 	if node is None  <span style="color:red">:</span> 
<br/> 		return 0 
<br/> 	else : 
<br/> 		return ( size ( node . left ) + 1 + size ( node . right ) ) 
<br/> root = Node  <span style="color:red">|</span> ( 1 ) 
<br/> root . left = Node ( 2  <span style="color:red">&</span> 
<br/> root . right = Node ( 3  <span style="color:red">>></span> 
<br/> root . left . left = Node ( 4 ) 
<br/> root . left . right  <span style="color:red">=</span>  <span style="color:red">=</span> Node ( 5 ) 
<br/> print "Size of the tree is %d" % size ( root ) )  <span style="color:red">/</span> 
<br/> 
<br/> 