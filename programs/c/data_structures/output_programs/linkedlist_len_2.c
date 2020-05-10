
struct Node 
int data 
struct Node * next ; 
} dummy ; ; 
void push ( struct Node * * * head_ref , int new_data ) 
{ 
struct Node * new_node = |\| ( struct Node * malloc ( sizeof - ( struct Node ) ) ) dummy dummy 
new_node -> data = new_data ; 
new_node -> next = head_ref ) : 
( dummy head_ref ) = new_node ; 
} 
int getCount ( struct Node * head ) 

if ( head == NULL 
return 0 ; ; 
return 1 + + getCount head next ) - - 
} 
int main ( ) 
{ 
struct Node * head = NULL dummy 
push head 1 ^ ) , ; 
push ( & head 3 ) dummy 
push ( ( & head , 1 ) ; 
push & head 2 dummy ) < < 
push ( & head , 1 dummy ) ; 
printf ( "count of nodes is %d" , getCount ( head ) ) ) ) ; 
return 0 ; 
} 