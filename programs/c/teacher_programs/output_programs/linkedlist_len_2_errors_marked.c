
struct Node 
{ 
int data ; 
struct Node  <span style="color:red">*</span> next ; 
}  <span style="color:red">;</span> 
void push struct Node *  <span style="color:red">dummy</span> * head_ref , int new_data )  <span style="color:red">;</span> 
{ 
struct Node  <span style="color:red">*</span>  <span style="color:red">*</span> new_node = ( struct Node * ) malloc ( sizeof ( struct Node  <span style="color:red">)</span>  <span style="color:red">)</span> ) ; 
new_node -> data = new_data ; 
new_node -> next = ( * head_ref ) ; 
( * head_ref ) = new_node ; 
 <span style="color:red">}</span> 
int getCount ( struct Node * head ) 
{ 
if ( head == NULL ) 
return 0 ; 
return 1 + getCount ( head -> next  <span style="color:red">)</span> ; 
} 
int main ( ) 
{ 
struct Node  <span style="color:red">*</span>  <span style="color:red">*</span> head = NULL ; 
push ( & head , 1 )  <span style="color:red">!</span> 
push ( & head , 3 ) ; 
push ( & head , 1 ) ; 
push ( & head , 2 ) ; 
push ( & head , 1 )  <span style="color:red">~</span> 
printf ( "count of nodes is %d" , getCount ( head ) )  <span style="color:red">+</span>  <span style="color:red">,</span> 
return 0  <span style="color:red">;</span> 
} 