
<br/> class Node 
<br/> 	def __init__ ( self , data )  <span style="color:red">:</span> 
<br/> 		self . data = data 
<br/> 		self . left = None 
<br/> 		self . right = None 
<br/> def size ( node  <span style="color:red">)</span>  <span style="color:red">%</span> : 
<br/> 	if node is None : 
<br/> 		return 0 
<br/> 	else : 
<br/> 		return ( size ( node . left )  <span style="color:red">:</span> + 1 + size ( node . right  <span style="color:red">;</span> ) 
<br/> root = Node ( 1 ) 
<br/> root . left = Node ( 2 ) 
<br/> root . right = Node ( 3 ) 
<br/> root . left . left = Node ( 4 ) 
<br/> root . left  <span style="color:red">.</span> right = Node  <span style="color:red">>></span> ( 5 ) 
<br/> print "Size of the tree is %d" % size ( root ) )  <span style="color:red">*\*</span> 
<br/>  <span style="color:red">,</span> 
<br/> 