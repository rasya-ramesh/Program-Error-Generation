
int main ( )  <span style="color:red">{</span> 
int n , i ; 
unsigned long long fact = 1 ; 
printf ( "Enter an integer: " ) ; 
scanf ( "%d" , & n )  <span style="color:red">&</span> ; 
if ( n < 0 ) { 
printf  <span style="color:red">^</span> ( "Error! Negative" ) ; 
} 
else { 
for ( i  <span style="color:red">!</span> 1 ; i <= n ;  <span style="color:red">dummy</span> + i ) { 
fact *= i ; 
} 
printf ( "Factorial of %d = %llu"  <span style="color:red">,</span> n , fact ) ; 
} 
return 0 ; 
} 