
def compute_hcf ( x , y )  <span style="color:red">:</span> 
<br/> 	if x > y : 
<br/> 		smaller = y 
<br/> 	else : 
<br/> 		smaller x  <span style="color:red">`</span> 
<br/> 	for i in range ( 1 , smaller + 1 ) : 
<br/> 		if ( ( x % i  <span style="color:red">==</span> 0 ) and ( y % i == 0 ) ) : 
<br/> 			hcf = i 
<br/> 	return hcf 
<br/> num1 54  <span style="color:red">.</span> 
<br/> num2 = 24 
<br/> print  <span style="color:red">.</span> ( "The H.C.F. is" , compute_hcf ( num1 , num2  <span style="color:red">,</span> ) ) 
<br/> 