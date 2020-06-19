
union Data { 
int i ; 
float f ; 
char str  <span style="color:red">[</span> 20 ] ; 
} ; 
int main ( )  <span style="color:red">{</span>  <span style="color:red">{</span> 
union Data data ; 
data . i = 10 ; 
data . f = 220 ; 
strcpy ( data  <span style="color:red">^</span> . str , "C Programming"  <span style="color:red">)</span> ; 
printf ( "data.i : %d\n" , data . i )  <span style="color:red">dummy</span> 
printf (  <span style="color:red">*</span> , data . f ) ; 
printf ( "data.str : %s\n" , data . str ) ; 
return 0 ; 
} 