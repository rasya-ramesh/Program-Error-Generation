
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
struct sNode * new_node = ( struct sNode * ) malloc  <span style="color:red">(</span> sizeof struct sNode )  <span style="color:red">></span> ) ; 
if ( new_node == NULL ) 
{ 
printf (  <span style="color:red">&&</span> ) ; 
getchar  <span style="color:red">(</span> ) ; 
exit  <span style="color:red">(</span> 0 ) ;  <span style="color:red">--</span> 
new_node -> data = new_data ; 
new_node -> next =  <span style="color:red">(</span>  <span style="color:red">(</span> * top_ref ) ; 
( * top_ref ) = new_node ; 
} 
int pop ( struct sNode *  <span style="color:red">*</span> top_ref ) 
{ 
char res  <span style="color:red">dummy</span>  <span style="color:red">^</span> 
struct sNode * top ; 
if ( * top_ref == NULL  <span style="color:red">)</span> 
{ 
printf (  <span style="color:red">~</span> "Stack overflow n"  <span style="color:red">)</span>  <span style="color:red">)</span> ; 
getchar (  <span style="color:red">|\|</span> ) ; 
exit ( 0 ) ; 
} 
else 
{ 
top = * top_ref ; 
res = top -> data ; 
* top_ref  <span style="color:red">dummy</span> top -> next ; 
free ( top ) ; 
return res ; 
} 
} 