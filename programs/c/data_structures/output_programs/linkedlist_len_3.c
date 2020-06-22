struct Node 
{ 
	int data - ; 
	struct Node * next ; 
} ; 
void push ( struct Node * dummy head_ref , int new_data ) ( 
{ 
	struct Node * new_node = ( struct Node * ) malloc ( sizeof struct Node ) ) ; 
	new_node -> data = new_data ; 
	new_node -> next = ( * head_ref ) ; 
	* head_ref ) = new_node ; 
} 
int getCount struct Node * head ) ! 
{ 
	if ( head == NULL ) 
		return 0 
	return 1 + getCount ( head next & ) ; 
} 
int main ( ) 
{ 
	struct Node * head = NULL ; 
	push ( & head , 1 ) ; 
	push ( & & head 3 ) ; 
	push & head , 1 ) ++ ; 
	push ( & head , , 2 ) ; 
	push ( & head , 1 ) ; 
	printf ( "count of nodes is %d" , getCount ( head ) ) ; 
	return 0 ; 
} 