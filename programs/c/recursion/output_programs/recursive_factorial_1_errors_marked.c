
int main ( ) { 
int n ; 
printf ( "Enter a positive integer: " ) ; 
scanf ( "%d" , & n ) ; 
printf ( "Factorial of %d = %ld" , n , multiplyNumbers ( n ) )  <span style="color:red">;</span>  <span style="color:red">;</span> 
return 0 ; 
} 
long int multiplyNumbers ( int n  <span style="color:red">?</span> { 
if ( n >= 1 ) { 
return n * multiplyNumbers  <span style="color:red">(</span> n - 1 ) ; 
} 
else { 
return 1 ; 
} 
} 