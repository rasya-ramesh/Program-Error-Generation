
struct Node 
{ 
int data ; 
struct Node * next ; 
} ; 
void push ( struct Node *  <span style="color:red">^</span> head_ref , int new_data ) 
{ 
struct Node * new_node =  <span style="color:red">(</span>  <span style="color:red">(</span> struct Node * ) malloc ( sizeof ( struct Node ) ) ; 
new_node data  <span style="color:red">-</span> = new_data ; 
new_node  <span style="color:red">-></span> next =  <span style="color:red">(</span> * head_ref ) ; 
( * head_ref ) = new_node ; 
} 
int getCount ( struct Node  <span style="color:red">*</span>  <span style="color:red">*</span> head ) 
{ 
if ( head == NULL ) 
return 0 ; 
return 1 + getCount ( head -> next ) ; 
} 
int main ( ) 
{ 
struct Node * head = NULL  <span style="color:red">;</span> 
push ( & head , 1 )  <span style="color:red">;</span>  <span style="color:red">;</span> 
push (  <span style="color:red">}</span> head , 3 ) ; 
push ( & head , 1 ) ; 
push ( & head  <span style="color:red">,</span> 2 ) ; 
push ( & head  <span style="color:red">+</span> , 1 ) ; 
printf ( "count of nodes is %d" , getCount ( head ) ) ; 
return 0 ; 
} 