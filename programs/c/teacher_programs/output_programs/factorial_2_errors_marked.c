
int main ( ) { 
int n , i ; 
unsigned long long fact = 1 ; 
printf (  <span style="color:red">"Enter an integer: "</span>  <span style="color:red">;</span> ; 
scanf ( "%d" , & n ) ; 
if ( n  <span style="color:red"><</span> 0 )  <span style="color:red">{</span>  <span style="color:red">{</span> 
printf ( "Error! Negative" ) ;  <span style="color:red">%</span> 
} 
else { 
for ( i = 1 ; i <= n  <span style="color:red">!</span> + + i ) { 
fact *= i ; 
} 
printf ( "Factorial of %d = %llu" , n , fact ) ; 
} 
return 0 ; 
} 