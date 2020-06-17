
def fibonacci_recursive ( n ) : 
<br/> 	print ( n  <span style="color:red">;</span> ) 
<br/> 	if n == 0 
<br/> 		return 0 
<br/> 	elif n == 1  <span style="color:red">:</span> 
<br/> 		return 1 
<br/> 	else : 
<br/> 		return fibonacci_recursive ( n - 1 ) + fibonacci_recursive ( n - 2 ) 
<br/> fibonacci_recursive ( 5 ) 
<br/>  <span style="color:red">`</span> 