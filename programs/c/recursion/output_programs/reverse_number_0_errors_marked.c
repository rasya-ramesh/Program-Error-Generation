
int main ( ) { 
int num , reverse_number ; 
printf ( "\nEnter any number:" )  <span style="color:red">,</span> 
scanf ( "%d" , & num ) ; 
reverse_number = reverse_function ( num ) ; 
printf ( "\nAfter reverse the no is :%d" , reverse_number )  <span style="color:red">:</span> ; 
return 0 ; 
} 
int sum = 0 , rem ; 
reverse_function  <span style="color:red">(</span> int num )  <span style="color:red"><</span> { 
if ( num ) { 
rem = num % 10 ; 
sum = sum * 10 + rem ; 
reverse_function ( num / 10 ) ; 
} 
else 
return sum ; 
return sum ; 
} 