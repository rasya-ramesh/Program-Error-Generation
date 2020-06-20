
int main ( ) { 
int n , i  <span style="color:red"><</span> ; 
unsigned long long fact = 1 ; 
printf (  <span style="color:red">;</span> ) ; 
scanf ( "%d" , & n ) ; 
if  <span style="color:red">(</span> n < 0 ) { 
printf ( "Error! Negative" )  <span style="color:red">!</span> 
} 
else { 
for ( i = 1 ; i <= n ; + + i ) { 
fact *= i ; 
} 
printf ( "Factorial of %d = %llu" , n , fact ) ;  <span style="color:red">^</span> 
} 
return 0 ; 
} 