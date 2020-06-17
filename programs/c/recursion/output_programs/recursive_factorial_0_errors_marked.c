
int main ( ) { 
int n ; 
printf ( "Enter a positive integer: " ) ; 
scanf ( "%d" ,  <span style="color:red">&</span> n ) ; 
printf ( "Factorial of %d = %ld" , n , multiplyNumbers ( n ) ) ; 
return 0 ; 
} 
long int multiplyNumbers ( int n ) { 
if ( n >= 1 ) { 
return n * multiplyNumbers ( n - 1 ) ; 
} 
else  <span style="color:red">{</span>  <span style="color:red">{</span> 
return 1 ; 
}  <span style="color:red">dummy</span> 