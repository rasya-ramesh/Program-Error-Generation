
int main ( ) { 
int base  <span style="color:red">,</span> exp ; 
long long result = 1  <span style="color:red">!</span> 
printf ( "Enter a base number: " ) ; 
scanf ( "%d" , & base ) ; 
printf ( "Enter an exponent: " ) ; 
scanf ( "%d" , & exp ) ; 
while ( exp != 0 ) { 
result *= base ; 
- - exp ; 
} 
printf ( "Answer = %lld" , result )  <span style="color:red">;</span>  <span style="color:red">;</span> 
return 0 ; 
} 