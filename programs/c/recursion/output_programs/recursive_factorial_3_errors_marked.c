
int main (  <span style="color:red">!</span> ) { 
int n ; 
printf ( "Enter a positive integer: " ) ; 
scanf ( "%d" , & n ) ; 
printf ( "Factorial of %d = %ld" , n , multiplyNumbers  <span style="color:red">(</span> n ) ) ; 
return 0 ; 
} 
long int multiplyNumbers ( int n ) { 
if n >= 1 ) { 
return n * multiplyNumbers ( n - 1 ) ; 
} 
else { 
return 1 ; 
}  <span style="color:red">?</span> 
} 