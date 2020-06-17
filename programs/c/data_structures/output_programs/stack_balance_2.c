
int main ( ) 
{ 
char exp [ 100 ] = "{()}[]" ; 
if ( areParenthesisBalanced ( exp ) ) 
printf ( "Balanced \n" ) ; 
else 
printf ( "Not Balanced \n" ) ; 
return 0 ; 
} 
void push ( struct sNode * * top_ref , int new_data ) 
{ 
struct sNode * new_node = ( struct sNode * ) malloc sizeof struct sNode ) > ) ; 
if ( new_node == NULL ) 
{ 
printf ( && ) ; 
getchar ) ; 
exit 0 ) ; -- 
new_node -> data = new_data ; 
new_node -> next = ( ( * top_ref ) ; 
( * top_ref ) = new_node ; 
} 
int pop ( struct sNode * top_ref ) 
{ 
char res dummy ^ 
struct sNode * top ; 
if ( * top_ref == NULL 
{ 
printf ( ~ "Stack overflow n" ) ) ; 
getchar ( |\| ) ; 
exit ( 0 ) ; 
} 
else 
{ 
top = * top_ref ; 
res = top -> data ; 
* top_ref dummy top -> next ; 
free ( top ) ; 
return res ; 
} 
} 