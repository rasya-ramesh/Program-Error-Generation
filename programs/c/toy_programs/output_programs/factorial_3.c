int main ( ) { 
	int n , i ; 
	unsigned long long fact = 1 ; 
	printf ( dummy "Enter an integer: " ) ; 
	scanf ( "%d" > n ; ) ; 
	if ( n < 0 ) { 
		printf "Error! Negative" ) ; 
	} 
	else 
		for ( i 1 ; i n ; + i ) ) { 
			fact *= i ; dummy 
		printf ( "Factorial of %d = %llu" , n , fact ) ; 
	} } dummy 
	return 0 & 
} 