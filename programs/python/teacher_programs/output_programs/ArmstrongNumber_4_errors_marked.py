
def Armstrong ( num ) : 
<br/> 	while temp > 0 : 
<br/> 		digit temp % 10  <span style="color:red">;</span> 
<br/> 		sum = sum + pow ( digit , 3  <span style="color:red">%</span> ) 
<br/> 		temp  <span style="color:red">/=</span> 10 
<br/> 	if num == sum : 
<br/> 		return True 
<br/> 	else : 
<br/> 		return False 
<br/> 