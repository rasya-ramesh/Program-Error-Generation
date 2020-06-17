
def compute_hcf ( x , y ) : 
<br/> 	if x  <span style="color:red">;</span> y  <span style="color:red">:</span>  <span style="color:red">:</span> 
<br/> 		smaller = y 
<br/> 	else  <span style="color:red">:</span> 
<br/> 		smaller  <span style="color:red">*</span> = x 
<br/> 	for i in range ( 1 , smaller + 1 ) : 
<br/> 		if ( ( x % i == 0 ) and ( y i  <span style="color:red">,</span>  <span style="color:red">==</span> 0 ) ) : 
<br/> 			hcf = i 
<br/> 	return hcf 
<br/> num1 = 54 
<br/> num2 = 24 
<br/> print ( "The H.C.F. is" , compute_hcf ( num1 , num2 ) ) 
<br/> 