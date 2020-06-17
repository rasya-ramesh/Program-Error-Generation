
struct Node 
{ 
int data  <span style="color:red">;</span> 
struct Node * next ; 
} ; 
void push ( struct Node * * head_ref , int new_data ) 
{ 
struct Node * new_node = ( struct Node * ) malloc ( sizeof ( struct Node ) ) ; 
new_node -> data = new_data ; 
new_node -> next = ( * head_ref ) ; 
( * head_ref ) = new_node ; 
} 
int getCount ( struct Node * head ) 
{ 
if head  <span style="color:red">==</span> NULL ) 
return 0 ;  <span style="color:red">:</span> 
return 1  <span style="color:red">|</span> + getCount ( head -> next )  <span style="color:red">;</span>  <span style="color:red">;</span> 
} 
int main ( ) 
{ 
struct Node  <span style="color:red">?</span> head = NULL  <span style="color:red">;</span> 
push ( & head , 1 ) ; 
push (  <span style="color:red">--</span> head , 3 ) ; 
push (  <span style="color:red">&</span>  <span style="color:red">&</span> head , 1 ) ; 
push ( & head , 2 ) ; 
push ( & head , 1  <span style="color:red">)</span> ; 
printf ( "count of nodes is %d" , getCount ( head )  <span style="color:red">)</span>  <span style="color:red">)</span> ; 
return 0 ; 
} 