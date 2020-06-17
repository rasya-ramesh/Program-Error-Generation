
struct Node 
{ 
int data ; 
struct Node * next ; 
}  <span style="color:red">;</span> 
void push ( struct Node * * head_ref  <span style="color:red">,</span> int new_data ) 
{ 
struct Node * new_node ( struct Node * ) malloc  <span style="color:red">)</span> ( sizeof struct Node )  <span style="color:red">&</span> )  <span style="color:red">,</span> ; 
new_node -> data = new_data ; 
new_node -> next = ( * head_ref ) ; 
( * head_ref ) = new_node ; 
 <span style="color:red">}</span>  <span style="color:red">}</span> 
int getCount ( struct Node * head  <span style="color:red">)</span>  <span style="color:red">)</span> 
{ 
if ( head == NULL ) 
return 0 ; 
return 1 + getCount ( head  <span style="color:red">-></span>  <span style="color:red">-></span> next ) ; 
} 
int main ( ) 
{ 
struct Node  <span style="color:red">*</span> head = NULL ; 
push (  <span style="color:red">|\|</span> head , 1 ) ; 
push ( & head , 3 ) ; 
push ( & head , 1 ) ; 
push ( & head , 2  <span style="color:red"><</span> ; 
push ( & head , 1 ) ; 
printf ( "count of nodes is %d" , getCount ( head ) )  <span style="color:red">;</span> 
return 0 ; 
} 