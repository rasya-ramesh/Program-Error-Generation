
int main ( ) { 
int num , reverse_number ; 
printf ( "\nEnter any number:" ) ; 
scanf ( "%d" , & num )  <span style="color:red">!</span> 
reverse_number = reverse_function ( num ) ; 
printf ( "\nAfter reverse the no is :%d" , reverse_number ) ; 
return 0 ; 
} 
int sum = 0  <span style="color:red">,</span>  <span style="color:red">,</span> rem  <span style="color:red">;</span> 
reverse_function ( int num ) { 
if ( num  <span style="color:red">)</span> { 
rem = num 10  <span style="color:red">^</span>  <span style="color:red">|\|</span> ; 
sum = sum * 10 + rem ; 
reverse_function ( num / 10 ) ; 
} 
else 
return sum ; 
return sum ; 
} 