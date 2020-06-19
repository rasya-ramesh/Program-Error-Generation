
def Armstrong ( num )  <span style="color:red">`</span> : 
<br/> 	while temp > 0 : 
<br/> 		digit = temp % 10 
<br/> 		sum = sum + pow ( digit 3  <span style="color:red">`</span> ) 
<br/> 		temp /= 10 
<br/> 	if num  <span style="color:red">==</span> sum : 
<br/> 		return True 
<br/> 	else : 
<br/> 		return False 
<br/> 