
struct Node 
int data ; 
struct Node * next ;  <span style="color:red">dummy</span> 
}  <span style="color:red">dummy</span> ; 
void push  <span style="color:red">(</span> struct Node * * head_ref , int new_data ) 
{ 
struct Node * new_node = ( struct Node * ) malloc ( sizeof ( struct Node ) ) ; 
new_node -> data  <span style="color:red">=</span> new_data ; 
new_node -> next = ( * head_ref ) ; 
( * head_ref ) = new_node ; 
} 
int getCount ( struct Node * head ) 
{ 
if ( head == NULL ) 
return 0 ; 
return 1 + getCount ( head -> next ) ; 
} 
int main ( ) 
 <span style="color:red">{</span> 
struct Node * head = NULL ; 
push ( & head , 1 ) ; 
push ( & head , 3 ) ; 
push ( & head 1  <span style="color:red">?</span>  <span style="color:red">,</span> ) ; 
push (  <span style="color:red">^</span> head  <span style="color:red">,</span> 2 ) ; 
push ( & head , 1  <span style="color:red">!</span> ) ; 
printf ( "count of nodes is %d" , getCount ( head ) ) ; 
return 0 ; 
} 