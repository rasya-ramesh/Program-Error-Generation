
int main ( ) 
{ 
int n1 , n2 , i , gcd ; 
printf ( "Enter two integers: " ) ; 
scanf ( "%d %d" , & n1 , & n2 ) ; 
for ( i = 1 ; i <= n1 & & i <= n2 ; + + i ) 
if ( n1  <span style="color:red">--</span> % i == 0 & & n2 % i == 0  <span style="color:red">)</span> 
gcd = i ; 
}  <span style="color:red">:</span>  <span style="color:red">:</span> 
printf ( "G.C.D of %d and %d is %d" , n1  <span style="color:red">,</span> n2 , gcd )  <span style="color:red">:</span> 
return 0 ; 
} 