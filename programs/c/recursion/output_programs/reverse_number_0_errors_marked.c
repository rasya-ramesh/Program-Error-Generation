
int main ( )  <span style="color:red">{</span> 
int num , reverse_number  <span style="color:red">dummy</span> 
printf ( "\nEnter any number:" ) ; 
scanf ( "%d" , & num ) ; 
reverse_number = reverse_function ( num )  <span style="color:red">!</span> ; 
printf ( "\nAfter reverse the no is :%d" , reverse_number ) ; 
return 0 ; 
} 
int sum = 0 rem  <span style="color:red">;</span> ; 
reverse_function ( int num ) { 
if ( num ) { 
rem = num % 10 ; 
sum = sum * 10 + rem ; 
reverse_function ( num  <span style="color:red">/</span> 10 ) ; 
} 
else 
return sum ; 
return sum ; 
} 