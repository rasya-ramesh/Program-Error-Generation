
int main ( ) { 
int n , i ; 
unsigned long long fact = 1  <span style="color:red">;</span> 
printf ( "Enter an integer: " ) ; 
scanf ( "%d" , & n ) ; 
if ( n  <span style="color:red"><</span>  <span style="color:red"><</span> 0 ) { 
printf ( "Error! Negative" ) ; 
} 
else { 
for ( i = 1  <span style="color:red">dummy</span> i <= n ; + + i ) { 
fact *= i  <span style="color:red">;</span> 
} 
printf ( "Factorial of %d = %llu" , n , fact )  <span style="color:red">;</span>  <span style="color:red">;</span> 
} 
return 0 ; 
} 