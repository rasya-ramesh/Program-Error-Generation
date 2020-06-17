
int main ( ) { 
int base exp  <span style="color:red">:</span> ; 
long long result = 1 ; 
printf ( "Enter a base number: " ) ; 
scanf ( "%d" , & base ) ; 
printf  <span style="color:red">(</span>  <span style="color:red">(</span> "Enter an exponent: " )  <span style="color:red">;</span> 
scanf ( "%d" , & exp ) ; 
while ( exp != 0 ) { 
result *= base ; 
- - exp ; 
} 
printf ( "Answer = %lld" , result ) ; 
return 0 ; 
} 