
union Data { 
int i ; 
float f ; 
char str [ 20 ]  <span style="color:red">;</span>  <span style="color:red">;</span> 
} ; 
int main ( ) { 
union Data data ; 
data . i  <span style="color:red">;</span> 10 ; 
data . f = 220 ; 
strcpy ( data . str  <span style="color:red">*</span> , "C Programming" ) ; 
printf ( "data.i : %d\n"  <span style="color:red">,</span> data . i ) ; 
printf ( "data.f : %f\n" , data f  <span style="color:red">~</span>  <span style="color:red">)</span> ; 
printf ( "data.str : %s\n" , data . str ) ; 
return 0 ; 
} 