
def Armstrong ( num ) : 
<br/> 	while temp > 0  <span style="color:red">:</span> 
<br/> 		digit = temp % 10 
<br/> 		sum = sum + pow digit , 3 )  <span style="color:red">-</span> 
<br/> 		temp /= 10 
<br/> 	if num == sum : 
<br/> 		return True 
<br/> 	else : 
<br/> 		return False 
<br/> 