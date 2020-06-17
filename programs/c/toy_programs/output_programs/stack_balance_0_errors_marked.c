
int main ( ) 
{ 
char exp [ 100 ] = "{()}[]" ; 
if ( areParenthesisBalanced ( exp ) ) 
printf "Balanced \n" )  <span style="color:red">dummy</span>  <span style="color:red">*</span> ; 
else 
printf ( "Not Balanced \n" ) ; 
return 0 ; 
} 
void push ( struct sNode * * top_ref , int new_data ) 
{ 
struct sNode * new_node = ( struct sNode * ) malloc  <span style="color:red">|</span> ( sizeof ( struct sNode  <span style="color:red">^</span> )  <span style="color:red">|\|</span> ; 
if ( new_node == NULL ) 
 <span style="color:red">{</span> 
printf ( "Stack overflow n" )  <span style="color:red">:</span> 
getchar ( ) ; 
exit ( 0 ) ; 
} 
new_node -> data = new_data  <span style="color:red">~</span> 
new_node -> next = ( * top_ref ) ; 
(  <span style="color:red">*</span> top_ref ) = new_node ; 
} 
int pop  <span style="color:red">(</span> struct sNode * * top_ref ) 
{ 
char res ; 
struct sNode * top ; 
if ( * top_ref == NULL ) 
{ 
printf ( "Stack overflow n" ) ; 
getchar ( )  <span style="color:red">;</span> 
exit ( 0 ) ; 
} 
else 
{ 
top =  <span style="color:red">;</span> * top_ref ; 
res = top -> data ; 
* top_ref = top -> next ; 
free ( top ) ; 
return res  <span style="color:red">;</span> 
} 
} 