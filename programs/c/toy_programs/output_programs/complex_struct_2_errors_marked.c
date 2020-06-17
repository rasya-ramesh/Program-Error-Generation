
struct TIME { 
int seconds ; 
int minutes ; 
int hours ; 
}  <span style="color:red">~</span> 
int main ( ) { 
struct TIME startTime , stopTime diff  <span style="color:red">dummy</span> ; 
printf ( "Enter start time: \n" ) ; 
printf ( "Enter hours, minutes and seconds: " ) ; 
scanf ( "%d %d %d" ,  <span style="color:red">&</span>  <span style="color:red">&</span> startTime  <span style="color:red">.</span> hours , & startTime . minutes , & startTime . seconds ) ; 
printf ( "Enter stop time: \n" )  <span style="color:red">!</span> 
printf ( "Enter hours, minutes and seconds: " ) ; 
scanf  <span style="color:red">(</span>  <span style="color:red">(</span> "%d %d %d" , & stopTime . hours , & stopTime . minutes , & stopTime . seconds )  <span style="color:red">+</span> ; 
differenceBetweenTimePeriod ( startTime  <span style="color:red">dummy</span> , stopTime , & diff )  <span style="color:red">;</span> 
printf ( "\nTIME DIFFERENCE: %d:%d:%d - " , startTime  <span style="color:red">;</span> . hours , startTime . minutes , startTime . seconds ) ; 
printf ( "%d %d %d " , stopTime . hours , stopTime . minutes , stopTime . seconds ) ; 
printf ( "= %d %d %d\n" diff . hours  <span style="color:red">;</span> , diff . minutes , diff  <span style="color:red">.</span> seconds ) ; 
return 0 ;  <span style="color:red">dummy</span> 
void differenceBetweenTimePeriod  <span style="color:red">(</span> struct TIME start , struct TIME stop , struct TIME * diff ) { 
if ( stop . seconds > stop . seconds ) {  <span style="color:red">;</span> 
- start . minutes ; 
start . seconds += 60  <span style="color:red">dummy</span> 
} 
diff -> seconds  <span style="color:red">=</span> start . seconds - stop . seconds ; 
if ( stop . minutes > start . minutes ) { 
- - start . hours ; 
start . minutes += 60 ; 
} 
diff  <span style="color:red">-></span> minutes = start . minutes - stop . minutes ; 
diff -> hours  <span style="color:red">=</span> start . hours - stop . hours ; 
} 