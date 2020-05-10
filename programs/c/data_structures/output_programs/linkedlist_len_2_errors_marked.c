
struct Node 
int data  <span style="color:red">;</span> 
struct Node * next ; 
}  <span style="color:red">dummy</span>  <span style="color:red">;</span>  <span style="color:red">;</span> 
void push ( struct Node  <span style="color:red">*</span>  <span style="color:red">*</span> * head_ref , int new_data ) 
{ 
struct Node * new_node =  <span style="color:red">|\|</span> ( struct Node * malloc ( sizeof  <span style="color:red">-</span> ( struct Node  <span style="color:red">)</span>  <span style="color:red">)</span> )  <span style="color:red">dummy</span>  <span style="color:red">dummy</span> 
new_node -> data = new_data ; 
new_node -> next =  <span style="color:red">(</span>  <span style="color:red">*</span> head_ref )  <span style="color:red">:</span> 
(  <span style="color:red">dummy</span> head_ref ) = new_node ; 
} 
int getCount ( struct Node * head ) 
 <span style="color:red">{</span> 
if ( head == NULL  <span style="color:red">)</span> 
return 0  <span style="color:red">;</span>  <span style="color:red">;</span> 
return 1  <span style="color:red">+</span>  <span style="color:red">+</span> getCount head  <span style="color:red">-></span> next )  <span style="color:red">-</span>  <span style="color:red">-</span>  <span style="color:red">;</span> 
} 
int main ( ) 
{ 
struct Node * head = NULL  <span style="color:red">dummy</span> 
push  <span style="color:red">&</span> head 1  <span style="color:red">^</span> )  <span style="color:red">,</span> ; 
push ( & head  <span style="color:red">,</span> 3 )  <span style="color:red">dummy</span> 
push  <span style="color:red">(</span>  <span style="color:red">(</span> & head , 1 ) ; 
push & head 2  <span style="color:red">dummy</span> )  <span style="color:red"><</span>  <span style="color:red"><</span>  <span style="color:red">;</span> 
push ( & head , 1  <span style="color:red">dummy</span> ) ; 
printf ( "count of nodes is %d" , getCount ( head  <span style="color:red">)</span>  <span style="color:red">)</span>  <span style="color:red">)</span>  <span style="color:red">)</span> ; 
return 0 ; 
} 