
int main ( ) 
{ 
char exp [ 100 ] = "{()}[]" ; 
if ( areParenthesisBalanced ( exp ) ) 
printf ( "Balanced \n" ) ; 
else 
printf ( "Not Balanced \n" ) ; 
return 0 ; 
} 
void push ( struct sNode  <span style="color:red">*</span> * top_ref , int new_data ) 
struct sNode  <span style="color:red">*</span>  <span style="color:red">*</span> new_node = ( struct sNode * ) malloc ( sizeof ( struct sNode ) ) ; 
if ( new_node NULL  <span style="color:red">|</span> ) 
{ 
printf ( "Stack overflow n"  <span style="color:red">)</span>  <span style="color:red">)</span>  <span style="color:red">;</span>  <span style="color:red">;</span> 
getchar ( )  <span style="color:red">,</span> ; 
exit  <span style="color:red">(</span>  <span style="color:red">(</span> 0 ) ; 
} 
new_node -> data = new_data ; 
new_node -> next = ( * top_ref ) ; 
(  <span style="color:red">*</span> top_ref ) = new_node ; 
}  <span style="color:red">&&</span> 
int pop struct sNode * * top_ref  <span style="color:red">)</span>  <span style="color:red">&</span> 
 <span style="color:red">{</span> 
char res ; 
struct sNode * top ; 
if ( * top_ref == NULL ) 
{ 
printf ( "Stack overflow n" ) ; 
getchar (  <span style="color:red">)</span> ; 
exit ( 0 ) ; 
} 
else 
{ 
top = * top_ref ; 
res = top data  <span style="color:red">!</span> ; 
* top_ref  <span style="color:red">^</span> top -> next ; 
free ( top ) ; 
return res ; 
} 
} 