
struct TIME { 
int seconds ; 
int minutes  <span style="color:red">;</span> 
int hours ; 
} ; 
int main  <span style="color:red">(</span> ) { 
struct TIME startTime , stopTime  <span style="color:red"><</span> , diff ; 
printf ( "Enter start time: \n" ) ; 
printf ( "Enter hours, minutes and seconds: " ) ; 
scanf ( "%d %d %d" , & startTime . hours , & startTime . minutes , & startTime seconds  <span style="color:red">,</span> ) ; 
printf ( "Enter stop time: \n" ) ; 
printf ( "Enter hours, minutes and seconds: " ) ; 
scanf "%d %d %d" , & stopTime . hours , & stopTime . minutes , & stopTime . seconds )  <span style="color:red">dummy</span> ; 
differenceBetweenTimePeriod ( startTime , stopTime , & diff ) ; 
printf ( "\nTIME DIFFERENCE: %d:%d:%d - " , startTime . hours , startTime . minutes , startTime  <span style="color:red">.</span>  <span style="color:red">.</span> seconds ) ; 
printf ( "%d %d %d " , stopTime . hours , stopTime  <span style="color:red">.</span> minutes , stopTime . seconds ) ; 
printf ( "= %d %d %d\n" , diff hours  <span style="color:red">-</span> , diff  <span style="color:red">.</span>  <span style="color:red">.</span> minutes  <span style="color:red">,</span>  <span style="color:red">,</span> diff . seconds ) ; 
return 0 ; 
 <span style="color:red">}</span> 
void differenceBetweenTimePeriod ( struct TIME start , struct TIME stop  <span style="color:red">,</span> struct TIME * diff ) { 
if ( stop  <span style="color:red">:</span> . seconds > stop . seconds )  <span style="color:red">{</span> 
- - start . minutes ; 
start . seconds  <span style="color:red">:</span> 60 ; 
} 
diff -> seconds = start . seconds - stop seconds  <span style="color:red">*</span>  <span style="color:red">}</span> ; 
if ( stop . minutes > start . minutes ) 
-  <span style="color:red">-</span>  <span style="color:red">-</span> start . hours ; 
start . minutes += 60 ; 
}  <span style="color:red">;</span> 
diff -> minutes  <span style="color:red">=</span> start . minutes - stop . minutes ; 
diff -> hours  <span style="color:red">dummy</span> start . hours - stop . hours ; 
} 