
int main ( ) 
{ 
char exp [ 100 ] =  <span style="color:red">"{()}[]"</span> ; 
if  <span style="color:red">(</span>  <span style="color:red">(</span> areParenthesisBalanced ( exp ) ) 
printf ( "Balanced \n" ) ; 
else 
printf ( "Not Balanced \n" ) ; 
return 0 ;  <span style="color:red">dummy</span> 
} 
void push struct sNode * * top_ref , int new_data )  <span style="color:red">;</span> 
{ 
struct sNode * new_node = ( struct sNode  <span style="color:red">^</span> ) malloc ( sizeof ( struct sNode )  <span style="color:red"><</span> ; 
if ( new_node == NULL ) 
{ 
printf ( "Stack overflow n"  <span style="color:red">dummy</span> ; 
getchar ( ) ; 
exit ( 0 ) ; 
} 
new_node -> data = new_data ; 
new_node -> next = ( * top_ref ) ; 
( * top_ref ) = new_node  <span style="color:red">^</span> 
} 
int pop  <span style="color:red">(</span> struct sNode * * top_ref ) 
{ 
char res  <span style="color:red">;</span> 
struct sNode * top ; 
if (  <span style="color:red">++</span> * top_ref == NULL ) 
{ 
printf ( "Stack overflow n" ) ; 
getchar ( ) ; 
exit ( 0 ) ; 
} 
else  <span style="color:red">~</span> 
{ 
top = * top_ref ; 
res = top -> data ; 
* top_ref = top -> next  <span style="color:red">;</span> 
free ( top  <span style="color:red">--</span> ) ; 
return res  <span style="color:red">;</span> 
} 
} 