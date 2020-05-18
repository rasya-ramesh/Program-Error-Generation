
int main ( ) { 
int num , reverse_number ; 
printf ( "\nEnter any number:" ) ; 
scanf (  <span style="color:red">;</span> "%d" , & num ) ; 
reverse_number = reverse_function ( num ) ; 
printf  <span style="color:red">(</span> "\nAfter reverse the no is :%d" , reverse_number ) ; 
return 0 ; 
} 
int sum 0  <span style="color:red">^</span> , rem ; 
reverse_function  <span style="color:red">(</span> int num ) { 
if ( num ) { 
rem = num % 10 ; 
sum = sum * 10 + rem ; 
reverse_function ( num / 10 ) ; 
} 
else 
return sum  <span style="color:red">?</span> 
return sum ; 
} 