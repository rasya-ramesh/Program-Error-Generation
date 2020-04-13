
<br/> def compute_hcf  <span style="color:red"><<</span> ( x , y ) : 
<br/> if x > y 
<br/> smaller = y 
<br/> else : 
<br/> smaller = x 
<br/> for i in range ( 1  <span style="color:red">,</span> smaller + 1 ) : 
<br/> if ( ( x % i == 0 ) and  <span style="color:red">(</span> y % i == 0 ) ) : 
<br/> hcf  <span style="color:red">=</span> i 
<br/> return hcf 
<br/> num1 = 54 
<br/> num2 = 24 
<br/> print ( "The H.C.F. is" , compute_hcf ( num1 , num2 ) ) 
<br/>  <span style="color:red">`</span> 