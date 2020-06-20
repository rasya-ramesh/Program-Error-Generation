
int main ( )  <span style="color:red">{</span>  <span style="color:red">{</span> 
int n i  <span style="color:red">!</span> ; 
unsigned long long fact = 1 ; 
printf ( "Enter an integer: " ) ; 
scanf ( "%d" , & n ) ; 
if ( n < 0 ) { 
printf ( "Error! Negative" ) ; 
 <span style="color:red">}</span> 
else 
for ( i = 1 ; i <= n ; + + i )  <span style="color:red">{</span> 
fact *= i ; 
} 
printf ( "Factorial of %d = %llu" , n , fact ) ; 
}  <span style="color:red">^</span> 
return 0 ; 
} 