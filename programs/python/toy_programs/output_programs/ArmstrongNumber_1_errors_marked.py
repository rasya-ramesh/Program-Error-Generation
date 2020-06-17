
def Armstrong ( num ) 
<br/> 	while temp > 0 : 
<br/> 		digit = temp % 10 
<br/> 		sum  <span style="color:red">=</span> sum + pow ( digit , 3 ) 
<br/> 		temp /= 10 
<br/> 	if num == sum : 
<br/> 		return True 
<br/> 	else  <span style="color:red">-</span> : 
<br/> 		return False 
<br/>  <span style="color:red">,</span> 