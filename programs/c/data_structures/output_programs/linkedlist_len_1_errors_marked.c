
struct Node  <span style="color:red">!</span> 
{ 
int data ; 
struct Node * next ; 
}  <span style="color:red">,</span>  <span style="color:red">dummy</span> 
void push  <span style="color:red">!</span> ( struct Node  <span style="color:red">*</span>  <span style="color:red">*</span> head_ref , int new_data ) 
struct Node * new_node = ( struct Node * ) malloc  <span style="color:red">(</span> sizeof struct Node )  <span style="color:red">~</span> ) ; 
new_node  <span style="color:red">-></span> data  <span style="color:red">=</span> new_data ; 
new_node -> next =  <span style="color:red">%</span> (  <span style="color:red">^</span> head_ref )  <span style="color:red">dummy</span> 
( * head_ref )  <span style="color:red">=</span> new_node ; 
}  <span style="color:red">+</span> 
int getCount struct Node * head )  <span style="color:red">|\|</span> 
{ 
if  <span style="color:red">(</span> head == NULL  <span style="color:red">)</span> 
return 0  <span style="color:red">~</span> 
return 1  <span style="color:red">~</span> + getCount ( head -> next ) ; 
} 
int main ( ) 
struct Node * head = NULL ; 
push (  <span style="color:red">&</span> head  <span style="color:red">%</span> , 1 )  <span style="color:red">;</span> 
push ( & head , 3 )  <span style="color:red">--</span> ; 
push  <span style="color:red">&</span> head 1  <span style="color:red">~</span> )  <span style="color:red">dummy</span> ; 
push  <span style="color:red">(</span>  <span style="color:red">&</span>  <span style="color:red">&</span> head , 2 ) ; 
push & head , 1 )  <span style="color:red">dummy</span>  <span style="color:red">!</span> ; 
printf ( "count of nodes is %d" , getCount ( head ) )  <span style="color:red">;</span>  <span style="color:red">;</span> 
return 0 ;  <span style="color:red">,</span> 
}  <span style="color:red">&&</span> 