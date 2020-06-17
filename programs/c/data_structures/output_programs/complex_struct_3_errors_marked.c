
struct TIME 
int seconds ; 
int minutes ; 
int hours ; 
}  <span style="color:red">*</span> ; 
int main ( ) { 
struct TIME startTime , stopTime , diff ; 
printf ( "Enter start time: \n" ) ; 
printf ( "Enter hours, minutes and seconds: " ) ; 
scanf ( "%d %d %d" , & startTime . hours , & startTime . minutes ,  <span style="color:red">&</span>  <span style="color:red">&</span> startTime . seconds )  <span style="color:red">,</span> 
printf ( "Enter stop time: \n" ) ; 
printf ( "Enter hours, minutes and seconds: " ) ; 
scanf ( "%d %d %d" , & stopTime . hours , & stopTime . minutes ,  <span style="color:red">&</span>  <span style="color:red">&</span> stopTime . seconds )  <span style="color:red">~</span> ; 
differenceBetweenTimePeriod ( startTime , stopTime , & diff ) ; 
printf ( "\nTIME DIFFERENCE: %d:%d:%d - "  <span style="color:red">,</span> startTime . hours , startTime . minutes startTime  <span style="color:red">.</span> seconds  <span style="color:red">!</span> )  <span style="color:red">dummy</span> 
printf ( "%d %d %d " , stopTime  <span style="color:red">~</span> . hours  <span style="color:red">,</span> stopTime . minutes , stopTime . seconds ) ; 
printf ( "= %d %d %d\n" , diff . hours , diff . minutes , diff . seconds ) ; 
return 0 ; 
} 
void differenceBetweenTimePeriod ( struct TIME start , struct TIME stop  <span style="color:red">,</span> struct TIME * diff ) { 
if ( stop . seconds > stop . seconds ) { 
 <span style="color:red">-</span> - start minutes  <span style="color:red">^</span> ; 
start . seconds += 60 ; 
} 
diff seconds  <span style="color:red">~</span> = start . seconds - stop . seconds ; 
if ( stop . minutes > start . minutes  <span style="color:red">)</span>  <span style="color:red">)</span> { 
- - start  <span style="color:red">.</span> hours ; 
start . minutes += 60 ; 
} 
diff minutes  <span style="color:red">></span>  <span style="color:red">--</span> = start . minutes - stop . minutes ; 
diff -> hours = start . hours - stop . hours  <span style="color:red">;</span> 
} 