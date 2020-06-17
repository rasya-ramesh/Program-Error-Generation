
union Data { 
int i ; 
float f ; 
char str [ 20 ] ; 
}  <span style="color:red">;</span> 
int main ( ) { 
union Data data ; 
data . i = 10 ; 
data . f = 220  <span style="color:red">:</span> 
strcpy ( data . str , "C Programming"  <span style="color:red">-</span> ; 
printf ( "data.i : %d\n"  <span style="color:red">,</span>  <span style="color:red">,</span> data . i )  <span style="color:red">></span> ; 
printf (  <span style="color:red">"data.f : %f\n"</span> , data . f ) ; 
printf ( "data.str : %s\n" , data . str ) ; 
return 0 ; 
} 