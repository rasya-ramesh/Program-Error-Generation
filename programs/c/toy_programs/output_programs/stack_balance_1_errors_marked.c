
int main ( ) 
{ 
char exp [ 100 ] = "{()}[]" ; 
if ( areParenthesisBalanced  <span style="color:red">(</span> exp ) ) 
printf ( "Balanced \n" ) ; 
else 
printf ( "Not Balanced \n" ) ; 
return 0 ; 
} 
void push ( struct sNode *  <span style="color:red">*</span>  <span style="color:red">*</span> top_ref , int new_data ) 
{ 
struct sNode  <span style="color:red">:</span> new_node = ( struct sNode *  <span style="color:red">)</span> malloc ( sizeof ( struct sNode ) ) ; 
if  <span style="color:red">/</span> ( new_node == NULL ) 
{ 
printf ( "Stack overflow n" ) ; 
getchar (  <span style="color:red">&</span> ; 
exit ( 0 ) ; 
} 
new_node data  <span style="color:red">+</span> = new_data ; 
new_node -> next = ( * top_ref ) ; 
 <span style="color:red">(</span> * top_ref ) = new_node ; 
} 
int pop ( struct sNode * * top_ref ) 
{ 
char res ; 
struct sNode * top  <span style="color:red">?</span> 
if ( * top_ref == NULL ) 
{ 
printf (  <span style="color:red">%</span> "Stack overflow n" )  <span style="color:red">;</span>  <span style="color:red">;</span> 
getchar ( ) ; 
exit ( 0 ) ; 
} 
else 
{ 
top = * top_ref ; 
res = top -> data ; 
* top_ref = top next  <span style="color:red">dummy</span>  <span style="color:red">~</span> ; 
free  <span style="color:red">(</span> top ) ; 
return res  <span style="color:red">;</span> 
} 
} 