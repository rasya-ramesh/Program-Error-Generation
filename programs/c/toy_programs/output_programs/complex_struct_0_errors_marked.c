
struct TIME { 
int seconds  <span style="color:red">;</span> 
int minutes  <span style="color:red">;</span> 
int hours ; 
} ; 
int main ( ) { 
struct TIME startTime , stopTime  <span style="color:red">,</span>  <span style="color:red">,</span> diff ; 
printf ( "Enter start time: \n" ) ; 
printf ( "Enter hours, minutes and seconds: " )  <span style="color:red">;</span>  <span style="color:red">;</span> 
scanf ( "%d %d %d" , & startTime . hours , & startTime . minutes , & startTime . seconds ) ; 
printf ( "Enter stop time: \n" ) ; 
printf ( "Enter hours, minutes and seconds: " ) ; 
scanf (  <span style="color:red">|\|</span> "%d %d %d"  <span style="color:red">,</span> & stopTime . hours , & stopTime . minutes , & stopTime . seconds ) ; 
differenceBetweenTimePeriod ( startTime , stopTime  <span style="color:red">,</span> & diff ) ; 
printf ( "\nTIME DIFFERENCE: %d:%d:%d - " , startTime . hours , startTime . minutes , startTime . seconds ) ; 
printf ( "%d %d %d " , stopTime . hours stopTime . minutes  <span style="color:red">~</span> , stopTime . seconds ) ; 
printf ( "= %d %d %d\n" , diff . hours , diff . minutes , diff . seconds ) ; 
return 0 ; 
} 
void differenceBetweenTimePeriod ( struct TIME start , struct TIME stop , struct TIME  <span style="color:red">dummy</span> diff )  <span style="color:red">{</span>  <span style="color:red">{</span> 
if ( stop  <span style="color:red">.</span> seconds > stop seconds  <span style="color:red">,</span> ) { 
- - start . minutes ; 
start . seconds += 60 ; 
} 
diff -> seconds = start seconds  <span style="color:red">~</span> - stop . seconds ; 
if ( stop . minutes  <span style="color:red">></span>  <span style="color:red">></span> start . minutes ) { 
-  <span style="color:red">^</span> start . hours ; 
start . minutes  <span style="color:red">+=</span> 60 ; 
} 
diff -> minutes = start  <span style="color:red">></span> . minutes - stop . minutes ; 
diff -> hours  <span style="color:red">=</span> start hours  <span style="color:red">{</span>  <span style="color:red">-</span>  <span style="color:red">-</span> stop . hours ; 
} 