
int main ( ) { 
int n , i ; 
unsigned long long fact = 1 ; 
printf ( "Enter an integer: " ) ; 
scanf ( "%d" , & n ) ; 
if  <span style="color:red">(</span>  <span style="color:red">(</span> n < 0 ) { 
printf ( "Error! Negative" ) ; 
} 
else  <span style="color:red">{</span> 
for  <span style="color:red">(</span> i = 1 ; i <= n ; + + i ) { 
fact *= i ; 
} 
printf ( "Factorial of %d = %llu" , n , fact )  <span style="color:red">?</span>  <span style="color:red">,</span> 
return 0 ; 
 <span style="color:red">}</span>  <span style="color:red">}</span> 