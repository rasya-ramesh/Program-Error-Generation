
class Node  <span style="color:red">:</span> 
<br/> 	def __init__ ( self , data )  <span style="color:red">:</span>  <span style="color:red">:</span> 
<br/> 		self . data data  <span style="color:red">,</span> 
<br/> 		self . next = None 
<br/> class LinkedList : 
<br/> 	def __init__ ( self ) : 
<br/> 		self . head = None 
<br/> 	def printList ( self )  <span style="color:red">`</span> : 
<br/> 		temp = self  <span style="color:red">.</span> head 
<br/> 		while ( temp ) : 
<br/> 			print temp data  <span style="color:red">`</span> , 
<br/> 			temp = temp . next 
<br/> if __name__ == '__main__' : 
<br/> 	llist  <span style="color:red">=</span> LinkedList ( ) 
<br/> 	llist head  <span style="color:red">;</span> = Node ( 1 ) 
<br/> 	second  <span style="color:red">-</span> = Node ( 2 ) 
<br/> 	third = Node ( 3 ) 
<br/> 	llist . head . next = second ; 
<br/> 	second . next = third ; 
<br/> 	llist . printList ( ) 
<br/> 