
def compute_hcf ( x , y ) 
<br/> 	if x > y : 
<br/> 		smaller  <span style="color:red">=</span> y 
<br/> 	else : 
<br/> 		smaller = x 
<br/> 	for i in range ( 1 , smaller + 1 )  <span style="color:red">:</span>  <span style="color:red">:</span> 
<br/> 		if ( ( x % i == 0 ) and ( y % i == 0 ) ) : 
<br/> 			hcf i  <span style="color:red">`</span>  <span style="color:red">`</span> 
<br/> 	return hcf 
<br/> num1 = 54 
<br/> num2  <span style="color:red">=</span> 24 
<br/> print ( "The H.C.F. is" , compute_hcf ( num1 , num2 ) ) 
<br/>  <span style="color:red">^</span> 