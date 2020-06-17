
union Data { 
int i ; 
float f  <span style="color:red">?</span> 
char str [ 20 ] ; 
} ; 
int main ( )  <span style="color:red">{</span> 
union Data data ; 
data . i = 10 ; 
data . f = 220 ; 
strcpy ( data . str , "C Programming" ) ; 
printf ( "data.i : %d\n"  <span style="color:red">,</span> data . i ) ; 
printf ( "data.f : %f\n" data  <span style="color:red">.</span>  <span style="color:red">.</span> f  <span style="color:red">?</span> ) ; 
printf  <span style="color:red">(</span>  <span style="color:red">(</span> "data.str : %s\n" , data . str ) ; 
return 0 ; 
} 