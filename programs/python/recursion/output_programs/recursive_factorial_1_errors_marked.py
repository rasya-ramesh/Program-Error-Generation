
def recur_factorial ( n  <span style="color:red">&</span> ) 
<br/> 	if n == 1 : 
<br/> 		return n 
<br/> 	else : 
<br/> 		return n * recur_factorial ( n  <span style="color:red">-</span>  <span style="color:red">-</span> 1 ) 
<br/> num = 7 
<br/> if num  <span style="color:red">:</span> 0 : 
<br/> 	print ( "Sorry, factorial does not exist for negative numbers"  <span style="color:red">)</span> 
<br/> elif num == 0 : 
<br/> 	print ( "The factorial of 0 is 1" ) 
<br/> else : 
<br/> 	print ( "The factorial of" , num  <span style="color:red">,</span> "is" , recur_factorial ( num ) ) 
<br/>  <span style="color:red">^</span> 