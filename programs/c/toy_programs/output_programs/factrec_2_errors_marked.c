
int main ( ) { 
int n  <span style="color:red">;</span> 
printf ( "Enter a positive integer: " ) ; 
scanf (  <span style="color:red"><</span> "%d" , & n ) ; 
printf ( "Factorial of %d = %ld" , n , multiplyNumbers ( n ) ) ; 
return 0 ; 
} 
long int multiplyNumbers ( int n ) { 
if ( n >= 1 ) { 
return n * multiplyNumbers ( n - 1 ) ; 
} 
else 
return 1 ; 
}  <span style="color:red">,</span> 
} 