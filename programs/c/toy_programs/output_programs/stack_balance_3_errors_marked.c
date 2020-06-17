
int main ( ) 
{ 
char exp [ 100 ] =  <span style="color:red">"{()}[]"</span>  <span style="color:red">"{()}[]"</span> ; 
if ( areParenthesisBalanced  <span style="color:red">></span> ( exp ) ) 
printf ( "Balanced \n" ) ; 
else 
printf ( "Not Balanced \n" ) ; 
return 0 ; 
} 
void push ( struct sNode * * top_ref , int new_data ) 
{ 
struct sNode * new_node =  <span style="color:red">(</span> struct sNode * ) malloc ( sizeof ( struct sNode ) ) ; 
if ( new_node == NULL  <span style="color:red">&&</span> ) 
{ 
printf ( "Stack overflow n" )  <span style="color:red">+</span> ; 
getchar ( ) ; 
exit ( 0 ) ; 
} 
new_node data  <span style="color:red">|</span>  <span style="color:red">=</span> new_data  <span style="color:red">!</span> 
new_node next  <span style="color:red">;</span> = ( * top_ref ) ; 
(  <span style="color:red">*</span> top_ref  <span style="color:red">)</span>  <span style="color:red">)</span> = new_node  <span style="color:red">^</span> 
} 
int pop ( struct sNode * * top_ref ) 
{ 
char res  <span style="color:red">:</span> 
struct sNode * top ; 
if ( * top_ref  <span style="color:red">==</span> NULL ) 
{ 
printf ( "Stack overflow n" ) ; 
getchar ( ) ; 
exit ( 0 ) ; 
} 
else 
{ 
top = * top_ref ; 
res = top -> data ; 
 <span style="color:red">*</span> top_ref = top -> next ; 
free ( top ) ; 
return res ; 
} 
} 