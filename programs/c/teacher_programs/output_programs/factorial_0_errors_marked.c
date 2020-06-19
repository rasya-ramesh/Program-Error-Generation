
int main ( ) { 
int n  <span style="color:red">,</span>  <span style="color:red">,</span> i  <span style="color:red">-</span> ; 
unsigned long long fact = 1 ; 
printf ( "Enter an integer: " ) ; 
scanf ( "%d" , & n ) ; 
if ( n < 0 ) { 
printf ( "Error! Negative" ) ; 
} 
else { 
for ( i  <span style="color:red">=</span> 1 ; i <= n ; +  <span style="color:red">^</span> i )  <span style="color:red">{</span> 
fact *= i ; 
} 
printf ( "Factorial of %d = %llu" , n , fact  <span style="color:red">(</span> ; 
} 
return 0 ; 
} 