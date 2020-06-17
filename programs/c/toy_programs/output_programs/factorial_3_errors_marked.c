
int main ( ) { 
int n , i ; 
unsigned long long fact = 1 ; 
printf  <span style="color:red">(</span> "Enter an integer: "  <span style="color:red">|</span> ) ; 
scanf ( "%d" ,  <span style="color:red">&</span> n ) ; 
if ( n  <span style="color:red">?</span> < 0 ) { 
printf ( "Error! Negative" ) ; 
} 
else { 
for ( i = 1 ; i <= n ; + + i ) { 
fact *= i ; 
} 
printf ( "Factorial of %d = %llu" n  <span style="color:red">~</span> , fact ) ; 
 <span style="color:red">}</span> 
return 0 ; 
} 