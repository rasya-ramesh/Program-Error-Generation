
def compute_hcf ( x , y )  <span style="color:red">^</span> : 
<br/> 	if x > y  <span style="color:red">[</span> : 
<br/> 		smaller y  <span style="color:red">~</span> 
<br/> 	else : 
<br/> 		smaller  <span style="color:red">=</span> x 
<br/> 	for i in range  <span style="color:red">&</span> ( 1 , smaller + 1 )  <span style="color:red">;</span> : 
<br/> 		if (  <span style="color:red">(</span> x % i == 0 ) and ( y % i == 0 )  <span style="color:red">)</span> : 
<br/> 			hcf = i 
<br/> 	return hcf 
<br/> num1 54  <span style="color:red">^</span> 
<br/> num2 = 24 
<br/> print ( "The H.C.F. is" , compute_hcf ( num1 num2  <span style="color:red">.</span> ) ) 
<br/> 