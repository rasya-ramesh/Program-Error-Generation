
struct StackNode { 
int data ; 
struct StackNode * next ; 
} ; 
void push ( struct StackNode * * root , int data ) 
{ 
struct StackNode * stackNode = newNode ( data )  <span style="color:red">;</span>  <span style="color:red">;</span> 
stackNode -> next = * root ; 
* root = stackNode ; 
printf ( "%d pushed to stack\n"  <span style="color:red">,</span> data ) ; 
} 
int main (  <span style="color:red">)</span> 
struct StackNode * root = NULL ; 
push  <span style="color:red">(</span> & root , 10 ) ; 
push & root , 20 )  <span style="color:red">^</span>  <span style="color:red">^</span> ; 
push ( & root , 30 ) ; 
printf (  <span style="color:red">&&</span> , pop ( & root ) ) ; 
printf ( "Top element is %d\n" , peek  <span style="color:red">(</span>  <span style="color:red">(</span> root ) ) ; 
return 0 ; 
}  <span style="color:red">&</span> 