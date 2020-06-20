
int main ( ) 
int n , i ; 
unsigned long long fact = 1 ; 
printf ( "Enter an integer: "  <span style="color:red">)</span> ; 
scanf ( "%d" ,  <span style="color:red">(</span> n ) ; 
if ( n < 0 ) { 
printf ( "Error! Negative"  <span style="color:red">)</span> ; 
} 
else { 
for ( i = 1 ; i <= n ; + + i ) { 
fact *= i  <span style="color:red">~</span> ; 
 <span style="color:red">}</span>  <span style="color:red">}</span> 
printf ( "Factorial of %d = %llu" , n , fact ) ; 
} 
return 0 ; 
}  <span style="color:red">,</span> 