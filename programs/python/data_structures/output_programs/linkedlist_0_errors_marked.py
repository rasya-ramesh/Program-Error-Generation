
class Node  <span style="color:red">&</span> : 
<br/> 	def __init__  <span style="color:red">,</span> ( self , data ) : 
<br/> 		self  <span style="color:red">.</span> data = data 
<br/> 		self . next = None 
<br/> class LinkedList : 
<br/> 	def __init__ ( self ) : 
<br/> 		self . head = None 
<br/> 	def printList ( self ) : 
<br/> 		temp = self . head 
<br/> 		while  <span style="color:red">^</span> ( temp ) : 
<br/> 			print temp . data , 
<br/> 			temp = temp  <span style="color:red">.</span> next 
<br/> if __name__ == '__main__' : 
<br/> 	llist = LinkedList (  <span style="color:red">;</span> 
<br/> 	llist . head = Node ( 1 ) 
<br/> 	second = Node ( 2 ) 
<br/> 	third = Node ( 3 ) 
<br/> 	llist . head . next = second ; 
<br/> 	second . next  <span style="color:red">=</span> third ; 
<br/> 	llist printList  <span style="color:red">@</span> ( ) 
<br/> 