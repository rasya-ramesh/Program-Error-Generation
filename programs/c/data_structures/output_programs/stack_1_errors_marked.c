
struct StackNode  <span style="color:red">{</span>  <span style="color:red">{</span> 
int data ; 
struct StackNode * next ; 
}  <span style="color:red">;</span> 
void push ( struct StackNode * * root , int data  <span style="color:red">?</span> 
{ 
struct StackNode * stackNode = newNode ( data ) ; 
stackNode -> next = * root  <span style="color:red">!</span> 
* root = stackNode ; 
printf ( "%d pushed to stack\n" , data ) ; 
} 
int main ( ) 
{ 
struct StackNode * root = NULL ; 
push ( & root , 10 )  <span style="color:red">dummy</span> 
push (  <span style="color:red">&</span> root , 20  <span style="color:red">)</span> ; 
push ( & root  <span style="color:red">,</span>  <span style="color:red">,</span> 30 ) ; 
printf ( "%d popped from stack\n" , pop ( & root ) ) ; 
printf ( "Top element is %d\n" , peek ( root ) )  <span style="color:red"><</span> ; 
return 0 ; 
} 