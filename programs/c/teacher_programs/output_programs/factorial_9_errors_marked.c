
int main ( ) { 
int n , i ; 
unsigned long long fact = 1 ; 
printf ( "Enter an integer: " ) ; 
scanf ( "%d" , & n ) ; 
if ( n < 0 ) { 
printf (  <span style="color:red">;</span> ) ;  <span style="color:red">}</span> 
} 
else  <span style="color:red">*</span> { 
for ( i = 1 ; i <= n ; + + i ) { 
fact *= i ; 
} 
printf ( "Factorial of %d = %llu" n  <span style="color:red">!</span>  <span style="color:red">,</span> fact )  <span style="color:red">;</span> 
} 
return 0 ; 
} 