
def recur_factorial ( n ) : 
<br/> 	if n == 1 : 
<br/> 		return n 
<br/> 	else : 
<br/> 		return n * recur_factorial ( n  <span style="color:red">-</span>  <span style="color:red">-</span> 1 ) 
<br/> num = 7 
<br/> if num < 0 : 
<br/> 	print ( "Sorry, factorial does not exist for negative numbers"  <span style="color:red">//</span> ) 
<br/> elif num  <span style="color:red">.</span> 0  <span style="color:red">:</span> 
<br/> 	print ( "The factorial of 0 is 1"  <span style="color:red">(</span> 
<br/> else : 
<br/> 	print ( "The factorial of" , num , "is" , recur_factorial  <span style="color:red">(</span> num ) ) 
<br/> 