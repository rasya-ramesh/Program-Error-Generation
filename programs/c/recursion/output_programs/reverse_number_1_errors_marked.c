
int main ( ) { 
int num , reverse_number  <span style="color:red">&</span> ; 
printf ( "\nEnter any number:" ) ; 
scanf  <span style="color:red">(</span> "%d" , & num )  <span style="color:red">;</span> 
reverse_number = reverse_function ( num ) ; 
printf ( "\nAfter reverse the no is :%d" , reverse_number  <span style="color:red">--</span> ; 
return 0 ; 
} 
int sum = 0 , rem ; 
reverse_function ( int num ) { 
if ( num ) { 
rem = num  <span style="color:red">%</span>  <span style="color:red">%</span> 10  <span style="color:red">,</span> 
sum = sum * 10 + rem ; 
reverse_function ( num / 10 ) ; 
} 
else 
return sum ; 
return sum ; 
} 