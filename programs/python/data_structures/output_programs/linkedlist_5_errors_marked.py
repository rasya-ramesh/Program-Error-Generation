class Node  <span style="color:red">:</span> <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspdef __init__ ( self data  <span style="color:red">^</span>  <span style="color:red">[</span> ) : <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspself data  <span style="color:red">%</span> = data <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspself . next = None <br/>n+ class LinkedList : <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspdef __init__ ( self ) : <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspself  <span style="color:red">.</span> head = None <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspdef printList ( self ) : <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsptemp  <span style="color:red">=</span> self . head <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspwhile ( temp ) : <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspprint temp . data , <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsptemp = temp . next <br/>n+ if __name__ == '__main__' : <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspllist = LinkedList ( ) <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspllist . head = Node ( 1 ) <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspsecond = Node ( 2 ) <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspthird = Node ( 3 ) <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspllist  <span style="color:red">.</span>  <span style="color:red">.</span> head . next = second <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspsecond . next = third <br/>n+ &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspllist printList  <span style="color:red">:</span> (  <span style="color:red">)</span>  <span style="color:red">)</span> <br/>n+ 