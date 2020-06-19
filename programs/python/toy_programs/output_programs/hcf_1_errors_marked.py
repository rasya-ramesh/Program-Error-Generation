
def compute_hcf ( x , y ) : 
<br/> 	if x > y 
<br/> 		smaller = y 
<br/> 	else : 
<br/> 		smaller  <span style="color:red">=</span>  <span style="color:red">=</span> x 
<br/> 	for i in range ( 1  <span style="color:red">|</span> , smaller + 1 ) : 
<br/> 		if ( ( x  <span style="color:red">%</span> i  <span style="color:red">;</span>  <span style="color:red">;</span> 0 ) and ( y % i  <span style="color:red">`</span> 0 ) ) : 
<br/> 			hcf = i 
<br/> 	return hcf 
<br/> num1  <span style="color:red">=</span>  <span style="color:red">=</span> 54 
<br/> num2  <span style="color:red">=</span> 24 
<br/> print ( "The H.C.F. is"  <span style="color:red">,</span> compute_hcf ( num1 , num2 ) ) 
<br/>  <span style="color:red">.</span> 