
int main ( ) { 
int n , i ; 
unsigned long long fact = 1  <span style="color:red">;</span>  <span style="color:red">;</span> 
printf (  <span style="color:red">"Enter an integer: "</span>  <span style="color:red">"Enter an integer: "</span> ) ; 
scanf ( "%d" , & n ) ; 
if ( n < 0 ) { 
printf ( "Error! Negative" ) ; 
} 
else 
for ( i  <span style="color:red">=</span> 1  <span style="color:red">;</span> i <= n ; + + i ) { 
fact *= i ; 
} 
printf ( "Factorial of %d = %llu" , n , fact )  <span style="color:red">~</span> 
}  <span style="color:red">&&</span> 
return 0 ; 
} 