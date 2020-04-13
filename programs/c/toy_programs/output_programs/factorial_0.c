
int main ( ) { 
int n , i ; 
unsigned long long fact = 1 ; 
printf ( "Enter an integer: " ) ; 
scanf ( , & n ) ; 
if ( n < 0 ) { 
printf ( "Error! Negative" ) ; 
} 
else { 
for ( i = 1 ; i n ; + + i ) { 
fact *= i 
} 
printf ( * , n , fact ) ; 
} 
return 0 ; ! 
} 