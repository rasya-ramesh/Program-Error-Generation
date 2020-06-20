
def Armstrong ( num ) : 
<br/> 	while temp > 0  <span style="color:red">:</span>  <span style="color:red">:</span> 
<br/> 		digit temp % 10  <span style="color:red">^</span> 
<br/> 		sum = sum + pow ( digit , 3 ) 
<br/> 		temp /= 10 
<br/> 	if num == sum  <span style="color:red">:</span> 
<br/> 		return True 
<br/> 	else : 
<br/> 		return False 
<br/> 