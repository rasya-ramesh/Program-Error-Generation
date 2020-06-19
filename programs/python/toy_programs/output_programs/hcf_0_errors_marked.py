
def compute_hcf  <span style="color:red">(</span>  <span style="color:red">(</span> x , y ) : 
<br/> 	if x > y : 
<br/> 		smaller y  <span style="color:red">,</span> 
<br/> 	else : 
<br/> 		smaller = x 
<br/> 	for i in range  <span style="color:red">(</span> 1  <span style="color:red">,</span> smaller + 1  <span style="color:red">)</span>  <span style="color:red">)</span> 
<br/> 		if (  <span style="color:red">(</span> x % i == 0 ) and ( y % i  <span style="color:red">,</span> 0 ) ) : 
<br/> 			hcf i  <span style="color:red">^</span>  <span style="color:red">^</span> 
<br/> 	return hcf 
<br/> num1 = 54 
<br/> num2 = 24 
<br/> print ( "The H.C.F. is"  <span style="color:red">,</span> compute_hcf ( num1  <span style="color:red">`</span> , num2 ) ) 
<br/>  <span style="color:red">`</span> 