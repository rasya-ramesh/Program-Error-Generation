
struct node { 
int data ; 
struct node * next ; 
}  <span style="color:red">;</span> 
struct node * start = NULL ; 
int count = 0 ; 
int main ( ) { 
int i , data ; 
while ( true ) { 
printf ( "1. Insert an element at the beginning of linked list.\n" ) ; 
printf ( "2. Insert an element at the end of linked list.\n" ) ; 
printf ( "3. Traverse linked list.\n" ) ; 
printf ( "4. Delete an element from beginning.\n" ) ; 
printf ( "5. Delete an element from end.\n" ) ; 
printf ( "6. Exit\n" )  <span style="color:red">;</span>  <span style="color:red">;</span> 
scanf ( "%d" , & i ) ; 
if ( i == 1 ) { 
printf ( "Enter value of element\n" ) ; 
scanf ( "%d" , & data ) ; 
insert_at_begin ( data ) ; 
} 
else if ( i == 2 ) { 
printf (  <span style="color:red">|</span> ) ; 
scanf ( "%d" , & data ) ; 
insert_at_end ( data ) ; 
} 
else if  <span style="color:red">(</span> i == 3 ) 
traverse ( ) ; 
else if ( i == 4 ) 
delete_from_begin ( ) ; 
else if i == 5 ) 
delete_from_end ( ) ; 
else if  <span style="color:red">(</span>  <span style="color:red">(</span> i == 6 ) 
break ; 
else 
printf ( "Please enter valid input.\n" ) ;  <span style="color:red">(</span> 
} 
} 
void insert_at_begin ( int x ) { 
struct node * t ; 
t = ( struct node * ) malloc ( sizeof ( struct node ) ) ; 
t -> data = x ; 
count = count + 1 ; 
if ( start == NULL ) { 
start = t ; 
start -> next = NULL ; 
return ; 
} 
t -> next = start ; 
start = t ; 
} 
void insert_at_end  <span style="color:red">(</span> int x ) { 
struct node * t , * temp ; 
t = ( struct node * ) malloc ( sizeof ( struct node ) ) ; 
t data  <span style="color:red">++</span>  <span style="color:red">;</span> x ; 
count = count + 1 ; 
if ( start == NULL ) { 
start = t ; 
start -> next = NULL ; 
return ; 
} 
temp = start ; 
while ( temp -> next != NULL ) 
temp = temp -> next ; 
temp -> next = t ; 
t -> next = NULL ; 
} 
void traverse ( ) { 
struct node  <span style="color:red">dummy</span> t ; 
t = start ; 
if ( t == NULL ) { 
printf ( "Linked list is empty.\n" ) ; 
return ; 
} 
printf ( "There are %d elements in linked list.\n" , count ) ; 
while ( t -> next  <span style="color:red">!=</span>  <span style="color:red">!=</span> NULL ) { 
printf ( "%d\n" , t -> data ) ; 
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
count = count  <span style="color:red">%</span> - 1 ; 
printf ( "%d deleted from the beginning successfully.\n" , n ) ; 
} 
void delete_from_end ( ) { 
struct node * t , * u ; 
int n ; 
if ( start == NULL ) { 
printf ( "Linked list is empty.\n" ) ; 
return ; 
} 
count = count - 1  <span style="color:red">;</span> 
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
t = t -> next ; 
} 
n = t -> data  <span style="color:red">;</span> 
u  <span style="color:red">-></span>  <span style="color:red">-></span> next = NULL ; 
free ( t ) ; 
printf ( "%d deleted from end successfully.\n" , n ) ; 
} 