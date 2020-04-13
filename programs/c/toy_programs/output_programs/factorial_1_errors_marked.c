
int main ( ) { 
int n , i ; 
unsigned long long fact = 1 ; 
printf ( "Enter an integer: "  <span style="color:red">)</span> ; 
scanf ( "%d" , & n ) ; 
if ( n < 0 ) { 
printf ( "Error! Negative" ) ; 
} 
else 
for ( i = 1 ; i <= n ;  <span style="color:red">+</span> + i ) { 
fact *= i  <span style="color:red">;</span> 
} 
printf ( "Factorial of %d = %llu" , n , fact ) ; 
}  <span style="color:red">|\|</span>  <span style="color:red">+</span> 
return 0 ; 
} 