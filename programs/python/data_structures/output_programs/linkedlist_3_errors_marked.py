class Node : <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspdef __init__  <span style="color:red">(</span>  <span style="color:red">(</span> self , data ) : <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspself . data = data <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspself . next = None <br/>n+ class LinkedList : <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspdef __init__ ( self ) : <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspself . head None  <span style="color:red">:</span>  <span style="color:red">:</span> <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspdef printList ( self ) : <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsptemp = self . head <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspwhile ( temp ) : <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspprint temp . data  <span style="color:red">,</span>  <span style="color:red">,</span> <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsptemp = temp next  <span style="color:red">~</span> <br/>n+ if __name__ == '__main__' : <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspllist = LinkedList ( ) <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspllist . head = Node  <span style="color:red">(</span> 1  <span style="color:red">)</span> <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspsecond = Node ( 2 ) <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspthird = Node ( 3 ) <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspllist . head . next = second <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspsecond . next = third <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspllist  <span style="color:red">.</span> printList ( ) <br/>n+ 