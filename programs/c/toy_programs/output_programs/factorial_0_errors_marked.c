
int main ( ) { 
int n , i ; 
unsigned long long fact = 1 ; 
printf ( "Enter an integer: " ) ; 
scanf (  <span style="color:red">"%d"</span> , & n ) ; 
if ( n < 0 ) { 
printf ( "Error! Negative" ) ; 
} 
else { 
for ( i = 1 ; i  <span style="color:red"><=</span> n ; + + i ) { 
fact *= i  <span style="color:red">;</span> 
} 
printf (  <span style="color:red">*</span> , n , fact ) ; 
} 
return 0 ;  <span style="color:red">!</span> 
} 