
union Data { 
int i ; 
float f  <span style="color:red">;</span> 
char str [ 20 ] ; 
}  <span style="color:red">;</span>  <span style="color:red">;</span> 
int main (  <span style="color:red">)</span> { 
union Data data ; 
data . i  <span style="color:red">,</span> 10 ; 
data . f = 220 ; 
strcpy ( data . str , "C Programming" )  <span style="color:red">dummy</span> 
printf ( "data.i : %d\n" , data . i ) ; 
printf ( "data.f : %f\n" , data . f ) ; 
printf ( "data.str : %s\n" , data . str ) ; 
return 0 ; 
} 