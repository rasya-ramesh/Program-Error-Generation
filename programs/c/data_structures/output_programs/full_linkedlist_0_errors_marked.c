
struct node { 
int data ; 
struct node * next  <span style="color:red">;</span>  <span style="color:red">;</span> 
} ; 
struct node * start = NULL ; 
int count  <span style="color:red">=</span> 0 ; 
int main ( ) { 
int i , data ; 
while ( true  <span style="color:red">)</span>  <span style="color:red">)</span> { 
printf ( "1. Insert an element at the beginning of linked list.\n" ) ; 
printf ( "2. Insert an element at the end of linked list.\n" ) ; 
printf "3. Traverse linked list.\n" )  <span style="color:red">++</span> ; 
printf ( "4. Delete an element from beginning.\n" ) ; 
printf ( "5. Delete an element from end.\n" ) ; 
printf "6. Exit\n" )  <span style="color:red">;</span> ; 
scanf ( "%d" , & i ) ; 
if ( i == 1 ) { 
printf ( "Enter value of element\n" ) ; 
scanf ( "%d" , & data ) ; 
insert_at_begin ( data ) ; 
} 
else if ( i == 2 ) { 
printf ( "Enter value of element\n" )  <span style="color:red">;</span> 
scanf ( "%d" , & data ) ; 
insert_at_end ( data ) ; 
} 
else if ( i == 3 ) 
traverse ( ) ; 
else if ( i == 4 ) 
delete_from_begin ( ) ; 
else if ( i == 5 ) 
delete_from_end ( ) ; 
else if ( i == 6 ) 
break ; 
else 
printf ( "Please enter valid input.\n" ) ; 
} 
} 
void insert_at_begin ( int x ) { 
struct node  <span style="color:red">!</span> t ; 
t = ( struct node * ) malloc ( sizeof ( struct node ) ) ; 
t -> data = x ; 
count = count + 1 ; 
if ( start NULL  <span style="color:red">dummy</span> ) 
start = t ; 
start -> next = NULL ; 
return ; 
}  <span style="color:red">{</span> 
t -> next = start ; 
start = t ; 
} 
void insert_at_end ( int x ) { 
struct node * t , * temp ; 
t = ( struct node * ) malloc ( sizeof ( struct node ) ) ; 
t -> data = x ; 
count = count + 1 ; 
if ( start == NULL ) { 
start = t ; 
start -> next = NULL ; 
return ; 
} 
temp = start ; 
while ( temp -> next != NULL ) 
temp = temp -> next ; 
temp -> next  <span style="color:red">=</span> t ; 
t -> next = NULL ; 
} 
void traverse ( ) { 
struct node * t ; 
t  <span style="color:red">=</span> start ; 
if ( t == NULL ) { 
printf ( "Linked list is empty.\n" ) ; 
return ;  <span style="color:red">dummy</span> 
} 
printf ( "There are %d elements in linked list.\n" , count ) ; 
while ( t -> next != NULL ) { 
printf ( "%d\n" , t  <span style="color:red">-></span> data ) ; 
t = t -> next ; 
} 
printf ( "%d\n" , t -> data ) ; 
} 
void delete_from_begin ( ) { 
struct node * t ; 
int n ; 
if ( start == NULL ) { 
printf ( "Linked list is empty.\n" ) ; 
return ; 
} 
n = start -> data ; 
t = start -> next ; 
free ( start ) ; 
start = t ; 
count = count - 1 ; 
printf ( "%d deleted from the beginning successfully.\n"  <span style="color:red">,</span>  <span style="color:red">,</span> n ) ; 
} 
void delete_from_end ( ) { 
struct node * t , * u ; 
int n ; 
if ( start == NULL ) { 
printf ( "Linked list is empty.\n" ) ; 
return ; 
} 
count = count - 1 ; 
if ( start -> next == NULL ) { 
n = start -> data ; 
free ( start ) ; 
start = NULL ; 
printf ( "%d deleted from end successfully.\n" , n ) ; 
return ; 
} 
t = start ; 
while ( t -> next != NULL ) { 
u = t ; 
t = t -> next ;  <span style="color:red">&&</span> 
} 
n = t -> data ; 
u -> next = NULL ; 
free ( t ) ; 
printf ( "%d deleted from end successfully.\n" , n ) ; 
} 