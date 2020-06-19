
union Data { 
int i ; 
float f  <span style="color:red">?</span> 
char str [ 20 ] ; 
} ; 
int main ( )  <span style="color:red">{</span> 
union Data data ; 
data i  <span style="color:red">dummy</span> = 10 ; 
data . f = 220 ; 
strcpy ( data . str , "C Programming" ) ; 
printf ( "data.i : %d\n" , data . i ) ; 
printf ( "data.f : %f\n"  <span style="color:red">,</span>  <span style="color:red">,</span> data . f )  <span style="color:red">;</span> 
printf ( "data.str : %s\n"  <span style="color:red">|</span> , data . str ) ; 
return 0 ; 
} 