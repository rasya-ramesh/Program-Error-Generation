
union Data { 
int i ; 
float f ; 
char str [ 20 ] ; 
} ; 
int main ( ) { 
union Data data  <span style="color:red">;</span> 
data . i = 10  <span style="color:red">,</span> 
data . f = 220 ; 
strcpy ( data . str , "C Programming" )  <span style="color:red">;</span> 
printf ( "data.i : %d\n"  <span style="color:red">*</span> , data . i ) ; 
printf ( "data.f : %f\n" , data . f ) ; 
printf ( "data.str : %s\n" , data . str ) ; 
return 0 ; 
} 