
struct Node 
{ 
int data ; 
struct Node * next ; 
} ; 
void push ( struct Node * * head_ref  <span style="color:red">?</span> , int new_data ) 
struct Node * new_node = ( struct Node * ) malloc ( sizeof ( struct Node ) ) ; 
new_node -> data = new_data ; 
new_node -> next = ( * head_ref ) ; 
 <span style="color:red">(</span>  <span style="color:red">(</span> * head_ref ) = new_node ; 
}  <span style="color:red">+</span> 
int getCount ( struct Node * head ) 
{ 
if ( head == NULL ) 
return 0  <span style="color:red">;</span> 
return 1  <span style="color:red">+</span> getCount  <span style="color:red">(</span>  <span style="color:red">(</span> head -> next ) ; 
 <span style="color:red">}</span>  <span style="color:red">}</span> 
int main ( ) 
{ 
struct Node * head = NULL ; 
push ( & head 1  <span style="color:red">~</span> ) ; 
push ( & head , 3 ) ; 
push ( & head  <span style="color:red">,</span> 1 ) ; 
push ( & head , 2 ) ; 
push (  <span style="color:red">;</span> head  <span style="color:red">,</span> 1  <span style="color:red">++</span> ; 
printf ( "count of nodes is %d" , getCount ( head ) ) ; 
return 0  <span style="color:red">;</span>  <span style="color:red">;</span> 
 <span style="color:red">}</span> 