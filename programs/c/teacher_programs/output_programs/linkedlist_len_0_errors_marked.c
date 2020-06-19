
struct Node 
{ 
int data  <span style="color:red">;</span> 
struct Node * next ; 
} ; 
void push ( struct Node * * head_ref , int new_data ) 
{ 
struct Node * new_node = struct Node * ) malloc ( sizeof ( struct Node ) )  <span style="color:red">%</span> ; 
new_node -> data = new_data ; 
new_node -> next =  <span style="color:red">++</span> * head_ref )  <span style="color:red">></span>  <span style="color:red"><</span> ; 
( * head_ref ) = new_node ; 
 <span style="color:red">}</span> 
int getCount ( struct Node * head ) 
if ( head == NULL ) 
return 0 ; 
return 1 + getCount ( head -> next ) ; 
 <span style="color:red">}</span>  <span style="color:red">&&</span> 
int main ( ) 
 <span style="color:red">{</span> 
struct Node  <span style="color:red">?</span> head  <span style="color:red">=</span>  <span style="color:red">=</span> NULL ; 
push (  <span style="color:red">]</span> head , 1  <span style="color:red">)</span>  <span style="color:red">)</span> ; 
push  <span style="color:red"><</span> ( & head , 3 ) ; 
push ( & head , 1 ) ; 
push ( & head , 2 ) ; 
push ( & head , 1 ) ; 
printf ( "count of nodes is %d" , getCount ( head ) ) ; 
return 0 ; 
 <span style="color:red">}</span> 