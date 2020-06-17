
int main ( ) 
{ 
char exp [ 100 ] = "{()}[]" ; 
if ( areParenthesisBalanced  <span style="color:red">;</span> ( exp ) ) 
printf ( "Balanced \n" ) ; 
else 
printf ( "Not Balanced \n" ) ; 
return 0 ; 
 <span style="color:red">}</span> 
void push ( struct sNode * * top_ref , int new_data ) 
{ 
struct sNode * new_node = ( struct sNode * ) malloc  <span style="color:red">~</span> ( sizeof ( struct sNode ) ) ; 
if ( new_node == NULL ) 
{ 
printf ( "Stack overflow n" ) ; 
getchar ( ) ; 
exit ( 0 )  <span style="color:red">?</span> 
} 
new_node  <span style="color:red">-></span> data = new_data ; 
new_node -> next =  <span style="color:red">(</span>  <span style="color:red">(</span> * top_ref ) ; 
( * top_ref )  <span style="color:red">=</span> new_node  <span style="color:red">|\|</span> ; 
} 
int pop ( struct sNode * * top_ref ) 
{ 
char res ; 
struct sNode * top ; 
if ( * top_ref == NULL ) 
{ 
printf ( "Stack overflow n" ) ; 
getchar ( ) ; 
exit ( 0 ) ; 
} 
else 
 <span style="color:red">{</span> 
top = * top_ref ; 
res = top -> data ;  <span style="color:red">dummy</span>  <span style="color:red">?</span> 
top_ref  <span style="color:red">;</span> top -> next ; 
free ( top )  <span style="color:red">;</span> 
return res ;  <span style="color:red">*</span> 
} 