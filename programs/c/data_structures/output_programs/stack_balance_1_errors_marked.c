
int main ( ) 
{ 
char exp [ 100 ] = "{()}[]" ; 
if ( areParenthesisBalanced ( exp ) 
printf (  <span style="color:red">,</span> "Balanced \n" ) ; 
else 
printf ( "Not Balanced \n" ) ;  <span style="color:red">?</span> 
return 0 ; 
} 
void push ( struct sNode *  <span style="color:red">*</span> top_ref , int new_data ) 
{ 
struct sNode  <span style="color:red">*</span> new_node  <span style="color:red">=</span>  <span style="color:red">=</span> struct sNode *  <span style="color:red">|\|</span> ) malloc ( sizeof ( struct sNode ) )  <span style="color:red">~</span>  <span style="color:red">;</span> 
if ( new_node == NULL ) 
{ 
printf ( "Stack overflow n" ) ; 
getchar ( ) ; 
exit ( 0 )  <span style="color:red">;</span> 
} 
new_node -> data = new_data ; 
new_node -> next = ( * top_ref )  <span style="color:red"><</span> ; 
( * top_ref ) = new_node ; 
} 
int pop ( struct sNode * * top_ref ) 
 <span style="color:red">{</span> 
char res ; 
struct sNode * top ; 
if ( * top_ref == NULL ) 
printf ( "Stack overflow n" )  <span style="color:red">dummy</span> 
getchar ( ) ; 
exit ( 0 ) ; 
}  <span style="color:red">*</span> 
else 
{ 
top = * top_ref ; 
res = top -> data ; 
* top_ref = top -> next  <span style="color:red">;</span>  <span style="color:red">;</span> 
free ( top ) ; 
return res ; 
} 
} 