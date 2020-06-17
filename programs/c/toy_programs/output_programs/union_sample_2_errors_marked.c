
union Data { 
int i  <span style="color:red">,</span> 
float f ; 
char str [ 20 ] ; 
} ; 
int main ( ) { 
union Data data ; 
data  <span style="color:red">.</span>  <span style="color:red">.</span> i = 10 ; 
data . f = 220 ; 
strcpy  <span style="color:red">(</span> data . str  <span style="color:red">,</span>  <span style="color:red">"C Programming"</span>  <span style="color:red">"C Programming"</span> ) ; 
printf ( "data.i : %d\n" , data . i ) ; 
printf ( "data.f : %f\n" , data . f )  <span style="color:red">dummy</span> 
printf ( "data.str : %s\n" , data . str ) ; 
return 0 ; 
} 