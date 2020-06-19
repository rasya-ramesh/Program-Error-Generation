
def Armstrong ( num ) 
<br/> 	while temp > 0 : 
<br/> 		digit = temp % 10 
<br/> 		sum = sum + pow  <span style="color:red">(</span> digit , 3 ) 
<br/> 		temp /= 10 
<br/> 	if num == sum  <span style="color:red">%</span> : 
<br/> 		return True 
<br/> 	else : 
<br/> 		return False 
<br/>  <span style="color:red">@</span> 