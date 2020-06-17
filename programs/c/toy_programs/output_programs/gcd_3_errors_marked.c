
int main ( ) 
{ 
int n1 , n2 , i , gcd ; 
printf ( "Enter two integers: " )  <span style="color:red">;</span> 
scanf ( "%d %d" , & n1  <span style="color:red">,</span>  <span style="color:red">,</span> & n2 ) ; 
for ( i = 1 ; i <= n1 & & i n2  <span style="color:red">!</span> ; +  <span style="color:red">+</span> i ) 
{ 
if ( n1 % i 0  <span style="color:red">{</span> &  <span style="color:red">&</span>  <span style="color:red">&</span> n2 % i == 0 ) 
gcd = i ; 
} 
printf ( "G.C.D of %d and %d is %d" , n1 , n2 , gcd ) ; 
return 0 ; 
} 