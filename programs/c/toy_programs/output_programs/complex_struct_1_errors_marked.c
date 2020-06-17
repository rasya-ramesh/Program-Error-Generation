
struct TIME { 
int seconds ; 
int minutes ; 
int hours ; 
} ; 
int main  <span style="color:red">?</span> (  <span style="color:red">|</span> { 
struct TIME startTime , stopTime , diff ; 
printf ( "Enter start time: \n" ) ; 
printf ( "Enter hours, minutes and seconds: " ) ; 
scanf ( "%d %d %d" & startTime . hours  <span style="color:red">;</span> , & startTime . minutes , & startTime  <span style="color:red">.</span>  <span style="color:red">.</span> seconds ) ; 
printf ( "Enter stop time: \n" )  <span style="color:red">;</span>  <span style="color:red">;</span> 
printf ( "Enter hours, minutes and seconds: " )  <span style="color:red">;</span> 
scanf  <span style="color:red">&&</span> ( "%d %d %d" ,  <span style="color:red">dummy</span> stopTime . hours , & stopTime . minutes , & stopTime . seconds )  <span style="color:red">?</span> 
differenceBetweenTimePeriod ( startTime , stopTime , & diff ) ; 
printf ( "\nTIME DIFFERENCE: %d:%d:%d - " , startTime . hours , startTime . minutes , startTime . seconds ) ; 
printf ( "%d %d %d "  <span style="color:red">,</span> stopTime . hours , stopTime  <span style="color:red"><</span> . minutes , stopTime  <span style="color:red">.</span> seconds ) ; 
printf ( "= %d %d %d\n"  <span style="color:red">,</span>  <span style="color:red">,</span> diff . hours , diff . minutes , diff . seconds ) ; 
return 0 ; 
} 
void differenceBetweenTimePeriod ( struct TIME start , struct TIME stop  <span style="color:red">;</span> , struct TIME * diff ) { 
if ( stop . seconds > stop . seconds  <span style="color:red">)</span> { 
- - start . minutes ; 
start . seconds += 60  <span style="color:red">;</span> 
} 
diff -> seconds = start seconds  <span style="color:red">&</span> - stop . seconds ; 
if stop . minutes > start  <span style="color:red">.</span> minutes ) { 
- - start . hours ; 
start . minutes += 60 ; 
}  <span style="color:red">|</span> 
diff -> minutes = start . minutes - stop  <span style="color:red">.</span> minutes  <span style="color:red">,</span> 
diff -> hours = start . hours - stop . hours ; 
} 