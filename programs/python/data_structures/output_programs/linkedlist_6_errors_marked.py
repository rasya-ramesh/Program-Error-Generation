class Node : <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspdef __init__ ( self , data ) : <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspself . data = data <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspself . next None  <span style="color:red">:</span> <br/>n+ class LinkedList  <span style="color:red">:</span> <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspdef __init__ ( self ) : <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspself . head = None <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspdef printList ( self )  <span style="color:red">:</span>  <span style="color:red">:</span> <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsptemp = self . head <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspwhile temp )  <span style="color:red">@</span>  <span style="color:red">*</span> : <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspprint temp . data , <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsptemp = temp next  <span style="color:red">~</span> <br/>n+ if __name__ == '__main__' : <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspllist = LinkedList ( ) <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspllist  <span style="color:red">.</span> head = Node ( 1 ) <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspsecond = Node ( 2 ) <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspthird = Node ( 3  <span style="color:red">)</span>  <span style="color:red">)</span> <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspllist . head . next = second <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspsecond . next = third <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspllist . printList  <span style="color:red">(</span> ) <br/>n+ 