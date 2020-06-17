
int main ( ) { 
int num , reverse_number ; 
printf ( "\nEnter any number:" ) ; 
scanf ( "%d" , & num ) ; 
reverse_number = reverse_function  <span style="color:red">(</span> num ) ; 
printf ( "\nAfter reverse the no is :%d" reverse_number  <span style="color:red">!</span> ) ; 
return 0 ; 
} 
int sum = 0 , rem ; 
reverse_function ( int num ) { 
if ( num ) { 
rem  <span style="color:red">=</span> num % 10 ; 
sum = sum * 10 + rem ; 
reverse_function ( num / 10 )  <span style="color:red">~</span>  <span style="color:red">+</span> 
} 
else 
return sum ; 
return sum ; 
} 