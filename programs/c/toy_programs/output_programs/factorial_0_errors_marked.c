
int main ( ) 
int n , i ; 
unsigned long long fact = 1  <span style="color:red">dummy</span> ; 
printf  <span style="color:red">(</span>  <span style="color:red">(</span> "Enter an integer: " ) ; 
scanf ( "%d" , & n ) ; 
if ( n < 0 ) { 
printf ( "Error! Negative" ) ; 
} 
else { 
for ( i  <span style="color:red">=</span> 1 ; i <= n ; + + i ) { 
fact  <span style="color:red">*=</span> i ; 
} 
printf ( "Factorial of %d = %llu" , n fact  <span style="color:red">?</span> ) ; 
} 
return 0 ; 
}  <span style="color:red">*</span> 