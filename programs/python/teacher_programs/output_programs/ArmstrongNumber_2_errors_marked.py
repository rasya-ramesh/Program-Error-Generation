
def Armstrong ( num ) : 
<br/> 	while temp > 0 
<br/> 		digit = temp % 10 
<br/> 		sum  <span style="color:red">=</span> sum  <span style="color:red">+</span>  <span style="color:red">+</span> pow ( digit , 3 ) 
<br/> 		temp /= 10 
<br/> 	if num == sum : 
<br/> 		return True 
<br/> 	else : 
<br/> 		return False 
<br/>  <span style="color:red">,</span> 