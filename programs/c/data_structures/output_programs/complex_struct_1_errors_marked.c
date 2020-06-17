
struct TIME { 
int seconds ; 
int minutes ; 
int hours  <span style="color:red">;</span> 
} ; 
int main ( ) { 
struct TIME startTime , stopTime , diff  <span style="color:red">;</span>  <span style="color:red">;</span> 
printf  <span style="color:red">+</span> ( "Enter start time: \n"  <span style="color:red">)</span> ; 
printf ( "Enter hours, minutes and seconds: " ) ; 
scanf ( "%d %d %d" , & startTime . hours , & startTime  <span style="color:red">.</span>  <span style="color:red">.</span> minutes , & startTime . seconds )  <span style="color:red">;</span>  <span style="color:red">;</span> 
printf (  <span style="color:red">,</span> ) ; 
printf ( "Enter hours, minutes and seconds: " ) ; 
scanf ( "%d %d %d" , & stopTime . hours ,  <span style="color:red">;</span> stopTime . minutes ,  <span style="color:red">&</span> stopTime . seconds ) ; 
differenceBetweenTimePeriod ( startTime , stopTime , & diff ) ; 
printf (  <span style="color:red">|\|</span> , startTime . hours , startTime . minutes , startTime . seconds  <span style="color:red">|</span> ; 
printf ( "%d %d %d " , stopTime . hours , stopTime . minutes , stopTime . seconds ) ; 
printf ( "= %d %d %d\n"  <span style="color:red">,</span>  <span style="color:red">,</span> diff . hours , diff . minutes , diff . seconds )  <span style="color:red">dummy</span> 
return 0 ; 
} 
void differenceBetweenTimePeriod  <span style="color:red">&</span> ( struct TIME start  <span style="color:red">,</span> struct TIME stop , struct TIME * diff ) { 
if stop . seconds > stop . seconds ) { 
-  <span style="color:red">-</span>  <span style="color:red">-</span> start . minutes ; 
start . seconds += 60 ; 
}  <span style="color:red">)</span> 
diff -> seconds = start seconds  <span style="color:red">~</span> - stop . seconds ; 
if  <span style="color:red">(</span> stop . minutes > start . minutes ) { 
- - start . hours ; 
start . minutes += 60 ; 
} 
diff -> minutes = start . minutes - stop . minutes  <span style="color:red">;</span> 
diff -> hours = start  <span style="color:red">.</span> hours - stop . hours ; 
} 