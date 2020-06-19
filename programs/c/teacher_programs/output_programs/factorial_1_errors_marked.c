
int main ( ) { 
int n , i ; 
unsigned long long fact = 1 ; 
printf ( "Enter an integer: " ) ; 
scanf ( "%d" , & n ) ; 
if ( n < 0 ) { 
printf  <span style="color:red">(</span> "Error! Negative" ) ; 
} 
else { 
for ( i = 1  <span style="color:red">[</span> ; i  <span style="color:red">,</span> <= n ; + + i ) { 
fact  <span style="color:red"><</span> i ; 
 <span style="color:red">}</span> 
printf ( "Factorial of %d = %llu" , n , fact ) ; 
} 
return 0  <span style="color:red">!</span> 
} 