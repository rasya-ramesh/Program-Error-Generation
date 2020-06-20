
int main  <span style="color:red">(</span> ) { 
int n , i ; 
unsigned long long fact = 1 ; 
printf  <span style="color:red">"Enter an integer: "</span> )  <span style="color:red">+</span> ; 
scanf ( "%d" , & n ) ; 
if ( n < 0 ) { 
printf ( "Error! Negative" ) ; 
} 
else { 
for  <span style="color:red">)</span> ( i = 1 ; i <= n ; + + i ) { 
fact *= i ; 
} 
printf ( "Factorial of %d = %llu"  <span style="color:red">&&</span> , n , fact  <span style="color:red">;</span> ; 
} 
return 0 ; 
} 