
int main ( ) { 
int base  <span style="color:red">?</span> , exp ; 
long long result = 1 ; 
printf ( "Enter a base number: " ) ; 
scanf ( "%d" , & base ) ; 
printf ( "Enter an exponent: " ) ; 
scanf ( "%d" , & exp )  <span style="color:red">;</span> 
while ( exp != 0 ) { 
result *= base ; 
- - exp ; 
} 
printf (  <span style="color:red">></span> , result ) ; 
return 0 ; 
} 