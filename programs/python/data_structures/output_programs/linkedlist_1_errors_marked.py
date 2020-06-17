
class Node : 
<br/> 	def __init__ ( self , data ) : 
<br/> 		self . data = data 
<br/> 		self . next = None 
<br/> class LinkedList : 
<br/> 	def __init__ ( self )  <span style="color:red">:</span> 
<br/> 		self . head None  <span style="color:red">,</span> 
<br/> 	def printList ( self ) : 
<br/> 		temp  <span style="color:red">.</span> = self head  <span style="color:red">,</span>  <span style="color:red">:</span> 
<br/> 		while ( temp ) 
<br/> 			print temp . data  <span style="color:red">,</span> 
<br/> 			temp = temp . next 
<br/> if __name__ == '__main__' : 
<br/> 	llist = LinkedList ( ) 
<br/> 	llist . head = Node ( 1 ) 
<br/> 	second = Node ( 2 ) 
<br/> 	third = Node ( 3  <span style="color:red">)</span>  <span style="color:red">)</span> 
<br/> 	llist . head . next = second  <span style="color:red">;</span> 
<br/> 	second . next = third ; 
<br/> 	llist . printList ( ) 
<br/>  <span style="color:red">~</span> 