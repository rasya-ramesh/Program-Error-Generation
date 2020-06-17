
struct Node 
 <span style="color:red">{</span> 
int data ; 
struct Node  <span style="color:red">,</span> next ; 
} ; 
void push  <span style="color:red">(</span> struct Node * * head_ref , int new_data ) 
struct Node * new_node = ( struct Node *  <span style="color:red">)</span> malloc ( sizeof ( struct Node )  <span style="color:red">dummy</span> ) ; 
new_node -> data = new_data ; 
new_node -> next =  <span style="color:red">(</span> * head_ref ) ; 
( * head_ref  <span style="color:red">~</span> ) = new_node ; 
}  <span style="color:red">{</span> 
int getCount ( struct Node * head ) 
{ 
if ( head == NULL ) 
return 0 ; 
return 1 + getCount  <span style="color:red">(</span>  <span style="color:red">(</span> head -> next ) ; 
} 
int main ( ) 
{ 
struct Node  <span style="color:red">:</span> head = NULL ; 
push ( & head , 1 ) ; 
push ( & head , 3 ) ; 
push ( & head , 1 ) ; 
push ( & head 2  <span style="color:red">:</span> ) ; 
push (  <span style="color:red">&</span>  <span style="color:red">&</span> head , 1 ) ; 
printf ( "count of nodes is %d" , getCount ( head ) ) ; 
return 0 ; 
} 