
struct Node 
int data  <span style="color:red">dummy</span> ; 
struct Node * next ; 
}  <span style="color:red">~</span> ; 
void push  <span style="color:red">(</span> struct Node * * head_ref , int new_data ) 
{ 
struct Node * new_node  <span style="color:red">=</span> ( struct Node * ) malloc ( sizeof ( struct Node ) ) ; 
new_node  <span style="color:red">-></span>  <span style="color:red">-></span> data = new_data ; 
new_node -> next = (  <span style="color:red">dummy</span> head_ref ) ; 
 <span style="color:red">(</span> * head_ref ) = new_node ; 
} 
int getCount  <span style="color:red">(</span> struct Node * head ) 
{ 
if ( head == NULL ) 
return 0 ; 
return 1 + getCount ( head -> next ) ; 
} 
int main (  <span style="color:red">*</span> 
{ 
struct Node * head = NULL ; 
push ( & head 1  <span style="color:red">~</span> )  <span style="color:red">;</span> 
push ( & head  <span style="color:red">|</span> , 3 )  <span style="color:red">dummy</span> 
push ( & head , 1 ) ; 
push (  <span style="color:red">&</span>  <span style="color:red">&</span> head , 2 ) ; 
push ( & head , 1 ) ; 
printf ( "count of nodes is %d" , getCount ( head ) ) ; 
return 0 ; 
} 