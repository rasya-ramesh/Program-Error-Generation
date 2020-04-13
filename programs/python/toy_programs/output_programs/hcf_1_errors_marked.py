
<br/> def compute_hcf ( x , y ) : 
<br/> if x > y : 
<br/> smaller = y 
<br/> else : 
<br/> smaller x  <span style="color:red">:</span> 
<br/> for i in range  <span style="color:red">(</span> 1 , smaller  <span style="color:red">+</span> 1 ) : 
<br/> if ( ( x % i == 0 ) and ( y % i == 0 ) ) : 
<br/> hcf  <span style="color:red">|</span> = i 
<br/> return hcf 
<br/> num1 = 54 
<br/> num2 = 24 
<br/> print ( "The H.C.F. is"  <span style="color:red">,</span> compute_hcf ( num1 , num2 ) ) 
<br/> 