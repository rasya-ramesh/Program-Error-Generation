
union Data { 
int i ; 
float f ; 
char str [ 20 ] ; 
}  <span style="color:red">;</span> 
int main  <span style="color:red">(</span> ) 
union Data data ; 
data . i = 10 ; 
data . f = 220 ; 
strcpy  <span style="color:red">(</span>  <span style="color:red">(</span> data . str , "C Programming" ) ; 
printf ( "data.i : %d\n" , data . i ) ; 
printf ( "data.f : %f\n" , data . f ) ; 
printf ( "data.str : %s\n" data . str  <span style="color:red">!</span> ) ; 
return 0 ; 
}  <span style="color:red">dummy</span> 