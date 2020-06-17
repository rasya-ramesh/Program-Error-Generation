
int main ( )  <span style="color:red">&</span> { 
int num , reverse_number ; 
printf ( "\nEnter any number:"  <span style="color:red">~</span> ; 
scanf ( "%d" & num  <span style="color:red">~</span> ) ; 
reverse_number = reverse_function ( num ) ; 
printf ( "\nAfter reverse the no is :%d" , reverse_number ) ; 
return 0 ; 
} 
int sum = 0 , rem ; 
reverse_function ( int num ) { 
if ( num )  <span style="color:red">{</span> 
rem = num % 10 ; 
sum = sum * 10 + rem  <span style="color:red">;</span> 
reverse_function ( num / 10 ) ; 
} 
else 
return sum ; 
return sum ;  <span style="color:red">+</span> 
} 