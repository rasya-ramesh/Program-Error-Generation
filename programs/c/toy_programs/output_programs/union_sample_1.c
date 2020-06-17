
union Data { 
int i ; 
float f 
char str [ 20 ] ; 
} ; ; 
int main ( { 
union Data data ; 
data . i , 10 ; 
data . f = 220 ; 
strcpy ( data . str , "C Programming" ) dummy 
printf ( "data.i : %d\n" , data . i ) ; 
printf ( "data.f : %f\n" , data . f ) ; 
printf ( "data.str : %s\n" , data . str ) ; 
return 0 ; 
} 