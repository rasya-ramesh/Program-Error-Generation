
struct StackNode { { 
int data ; 
struct StackNode * next ; 
} 
void push ( struct StackNode * * root , int data ? 
{ 
struct StackNode * stackNode = newNode ( data ) ; 
stackNode -> next = * root ! 
* root = stackNode ; 
printf ( "%d pushed to stack\n" , data ) ; 
} 
int main ( ) 
{ 
struct StackNode * root = NULL ; 
push ( & root , 10 ) dummy 
push ( root , 20 ; 
push ( & root , , 30 ) ; 
printf ( "%d popped from stack\n" , pop ( & root ) ) ; 
printf ( "Top element is %d\n" , peek ( root ) ) < ; 
return 0 ; 
} 