
union Data 
int i ; 
float f  <span style="color:red">;</span> 
char str [ 20 ] ; 
}  <span style="color:red">!</span>  <span style="color:red">!</span> ; 
int main ( ) { 
union Data data ; 
data . i = 10 ; 
data . f = 220 ; 
strcpy ( data . str , "C Programming" ) ; 
printf ( "data.i : %d\n" , data  <span style="color:red">.</span>  <span style="color:red">.</span> i  <span style="color:red">;</span> ; 
printf ( "data.f : %f\n" , data . f ) ; 
printf ( "data.str : %s\n" , data . str )  <span style="color:red">;</span> 
return 0 ; 
} 