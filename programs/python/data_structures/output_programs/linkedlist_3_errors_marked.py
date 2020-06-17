
class Node  <span style="color:red">:</span>  <span style="color:red">:</span> 
<br/> 	def __init__  <span style="color:red">(</span> self , data ) : 
<br/> 		self . data = data 
<br/> 		self . next = None 
<br/> class LinkedList : 
<br/> 	def __init__ ( self )  <span style="color:red">:</span>  <span style="color:red">:</span> 
<br/> 		self . head = None 
<br/> 	def printList ( self ) : 
<br/> 		temp = self . head 
<br/> 		while ( temp ) : 
<br/> 			print temp . data , 
<br/> 			temp  <span style="color:red">=</span> temp . next 
<br/> if __name__ == '__main__' 
<br/> 	llist = LinkedList (  <span style="color:red">@</span> 
<br/> 	llist . head  <span style="color:red">=</span> Node 1 )  <span style="color:red">//</span> 
<br/> 	second = Node ( 2 ) 
<br/> 	third = Node ( 3 ) 
<br/> 	llist . head . next = second ; 
<br/> 	second  <span style="color:red">,</span> . next = third ; 
<br/> 	llist . printList ( ) 
<br/>  <span style="color:red">%</span> 