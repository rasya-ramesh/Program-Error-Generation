
struct Node 
{ 
int data  <span style="color:red">&&</span>  <span style="color:red">?</span> 
struct Node  <span style="color:red">~</span> * next ;  <span style="color:red">^</span>  <span style="color:red">|\|</span> 
; 
void push ( struct Node *  <span style="color:red">dummy</span> head_ref , int new_data ) 
{ 
struct Node * new_node = ( struct Node  <span style="color:red">%</span> * malloc  <span style="color:red">(</span> sizeof ( struct Node ) )  <span style="color:red">--</span>  <span style="color:red">;</span> 
new_node  <span style="color:red">-></span> data = new_data ; 
new_node -> next = (  <span style="color:red">*</span> head_ref  <span style="color:red">)</span>  <span style="color:red">!</span> 
( * head_ref ) = new_node  <span style="color:red">;</span>  <span style="color:red">;</span> 
 <span style="color:red">}</span> 
int getCount  <span style="color:red">(</span> struct Node * head  <span style="color:red">-</span> ) 
{ 
if ( head == NULL  <span style="color:red">)</span> 
return 0  <span style="color:red">dummy</span> 
return 1 getCount ( head  <span style="color:red">|\|</span> -> next )  <span style="color:red">^</span>  <span style="color:red">*</span> ; 
 <span style="color:red">}</span> 
int main ( ) 
struct Node * head  <span style="color:red">=</span>  <span style="color:red">=</span> NULL ; 
push ( & head , 1 ) ; 
push  <span style="color:red">(</span>  <span style="color:red">&</span>  <span style="color:red">&</span> head , 3 ) ; 
push  <span style="color:red">(</span> & head , 1 ) ; 
push (  <span style="color:red">[</span> head  <span style="color:red">,</span> 2 )  <span style="color:red">!</span> 
push ( & head , 1  <span style="color:red">/</span> ; 
printf ( "count of nodes is %d" , getCount ( head ) )  <span style="color:red">;</span> 
return 0  <span style="color:red">:</span> 
}  <span style="color:red">~</span>  <span style="color:red">~</span> 