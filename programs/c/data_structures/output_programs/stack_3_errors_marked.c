
struct StackNode  <span style="color:red">{</span> 
int data ; 
struct StackNode * next ; 
} ; 
void push ( struct StackNode * * root , int data ) 
{ 
struct StackNode * stackNode = newNode ( data ) ; 
stackNode -> next =  <span style="color:red">*</span>  <span style="color:red">*</span> root ; 
* root = stackNode ; 
printf ( "%d pushed to stack\n" , data )  <span style="color:red">;</span>  <span style="color:red">~</span> 
int main ( ) 
struct StackNode * root = NULL ; 
push (  <span style="color:red">&</span>  <span style="color:red">&</span> root , 10 )  <span style="color:red">;</span> 
push ( & root , 20 ) ; 
push ( & root , 30 ) ; 
printf ( "%d popped from stack\n" , pop ( & root )  <span style="color:red">)</span>  <span style="color:red">)</span> ; 
printf ( "Top element is %d\n" , peek root )  <span style="color:red">[</span> ) ; 
return 0 ; 
}  <span style="color:red">:</span> 