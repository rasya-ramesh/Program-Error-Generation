
union Data 
int i ; 
float f ; 
char str [ 20 ] ; 
}  <span style="color:red">+</span> ; 
int main )  <span style="color:red">|</span> { 
union Data data ; 
data . i = 10 ; 
data . f  <span style="color:red">=</span> 220 ; 
strcpy ( data . str , "C Programming" ) ; 
printf ( "data.i : %d\n" , data . i ) ; 
printf ( "data.f : %f\n" , data . f  <span style="color:red">+</span> ) ; 
printf (  <span style="color:red">"data.str : %s\n"</span> , data . str )  <span style="color:red">;</span>  <span style="color:red">;</span> 
return 0 ; 
} 