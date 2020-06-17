
int main ( ) { 
int num , reverse_number ; 
printf ( "\nEnter any number:" ) ; 
scanf ( "%d"  <span style="color:red">!</span> , & num ) ; 
reverse_number  <span style="color:red">?</span> reverse_function ( num ) ; 
printf ( "\nAfter reverse the no is :%d" , reverse_number )  <span style="color:red">;</span> 
return 0 ; 
} 
int sum = 0 , rem ; 
reverse_function ( int num )  <span style="color:red">{</span> 
if ( num ) { 
rem = num % 10 ; 
sum = sum * 10 + rem ; 
reverse_function ( num / 10 ) ;  <span style="color:red">{</span> 
} 
else 
return sum  <span style="color:red">,</span> 
return sum ; 
} 