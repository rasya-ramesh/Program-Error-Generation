
struct StackNode { 
int data ; 
struct StackNode * next ;  <span style="color:red">></span> 
 <span style="color:red">;</span> 
void push ( struct StackNode * * root , int data ) 
 <span style="color:red">{</span> 
struct StackNode * stackNode = newNode ( data ) ; 
stackNode -> next = * root ; 
* root = stackNode ; 
printf ( "%d pushed to stack\n" data  <span style="color:red">^</span> ) ; 
} 
int main ( ) 
{ 
struct StackNode * root = NULL ; 
push ( & root , 10 ) ; 
push ( & root , 20 ) ; 
push (  <span style="color:red">-</span> & root , 30  <span style="color:red">-</span> ; 
printf ( "%d popped from stack\n"  <span style="color:red">,</span> pop ( & root ) ) ; 
printf (  <span style="color:red">,</span> "Top element is %d\n" , peek ( root ) )  <span style="color:red">;</span>  <span style="color:red">;</span> 
return 0 ; 
} 