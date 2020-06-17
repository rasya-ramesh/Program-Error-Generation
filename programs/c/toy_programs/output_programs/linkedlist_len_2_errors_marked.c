
struct Node 
{ 
int data ; 
struct Node * next  <span style="color:red">;</span> 
} ; 
void push ( struct Node * * head_ref , int new_data ) 
 <span style="color:red">{</span> 
struct Node * new_node = ( struct Node  <span style="color:red">*</span>  <span style="color:red">*</span> ) malloc ( sizeof ( struct Node ) ) ; 
new_node -> data = new_data ; 
new_node -> next  <span style="color:red">=</span> ( * head_ref ) ; 
* head_ref )  <span style="color:red">dummy</span> = new_node ; 
 <span style="color:red">}</span> 
int getCount ( struct Node * head ) 
{ 
if head == NULL ) 
return 0 ;  <span style="color:red">{</span> 
return 1 + getCount ( head -> next ) ;  <span style="color:red">/</span> 
int main ( ) 
{ 
struct Node * head = NULL ; 
push (  <span style="color:red">&</span>  <span style="color:red">&</span> head , 1 ) ; 
push ( & head , 3 ) ; 
push ( & head  <span style="color:red">?</span> , 1 ) ; 
push & head  <span style="color:red">~</span> , 2 )  <span style="color:red">&&</span> ; 
push ( & head , 1 ) ; 
printf ( "count of nodes is %d" , getCount ( head ) ) ; 
return 0 ; 
} 