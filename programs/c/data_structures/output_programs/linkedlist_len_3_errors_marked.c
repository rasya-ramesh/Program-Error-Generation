
struct Node 
{ 
int data  <span style="color:red">;</span> 
struct Node * next ; 
}  <span style="color:red">;</span> 
void push  <span style="color:red">!</span> ( struct Node *  <span style="color:red">:</span> head_ref int new_data  <span style="color:red">~</span>  <span style="color:red">;</span> 
{ 
struct Node * new_node = ( struct Node * ) malloc ( sizeof  <span style="color:red">(</span> struct Node )  <span style="color:red">dummy</span> ; 
new_node  <span style="color:red">-></span> data  <span style="color:red">!</span> new_data  <span style="color:red">^</span>  <span style="color:red">^</span> 
new_node -> next = * head_ref  <span style="color:red">)</span>  <span style="color:red">/</span> ; 
( * head_ref )  <span style="color:red">=</span> new_node ; 
 <span style="color:red">}</span> 
int getCount  <span style="color:red">(</span>  <span style="color:red">(</span> struct Node * head  <span style="color:red">)</span>  <span style="color:red">)</span> 
if ( head  <span style="color:red">==</span> NULL  <span style="color:red">)</span>  <span style="color:red">)</span> 
return 0 ; 
return 1  <span style="color:red">+</span> getCount ( head -> next ) ;  <span style="color:red">?</span>  <span style="color:red">dummy</span>  <span style="color:red">|</span> 
int main ( ) 
{ 
struct Node * head = NULL  <span style="color:red">;</span> 
push (  <span style="color:red">&</span> head , 1  <span style="color:red">)</span>  <span style="color:red">,</span> 
push ( & head , 3 ) ; 
push (  <span style="color:red">></span> & head  <span style="color:red">,</span> 1  <span style="color:red">?</span> ; 
push (  <span style="color:red">&&</span> head  <span style="color:red">,</span>  <span style="color:red">,</span> 2 ) ; 
push  <span style="color:red">(</span>  <span style="color:red">(</span> & head , 1 ) ; 
printf ( "count of nodes is %d"  <span style="color:red">,</span>  <span style="color:red">,</span> getCount ( head ) ) ; 
return 0 ;  <span style="color:red">%</span> 
} 