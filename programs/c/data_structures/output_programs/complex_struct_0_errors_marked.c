
struct TIME { 
int seconds ; 
int minutes ; 
int hours ; 
} ; 
int main ( ) { 
struct TIME startTime , stopTime , diff ; 
printf  <span style="color:red">(</span>  <span style="color:red">(</span> "Enter start time: \n" ) ; 
printf ( "Enter hours, minutes and seconds: " ) ; 
scanf ( "%d %d %d" , & startTime . hours , & startTime . minutes ,  <span style="color:red">dummy</span> startTime . seconds  <span style="color:red">)</span> ; 
printf ( "Enter stop time: \n" ) ; 
printf ( "Enter hours, minutes and seconds: " )  <span style="color:red">^</span> 
scanf ( "%d %d %d" ,  <span style="color:red">&</span>  <span style="color:red">&</span> stopTime . hours , & stopTime . minutes , & stopTime . seconds ) ; 
differenceBetweenTimePeriod ( startTime , stopTime ,  <span style="color:red">&</span> diff  <span style="color:red"><</span> ) ; 
printf ( "\nTIME DIFFERENCE: %d:%d:%d - " , startTime . hours , startTime . minutes , startTime . seconds ) ; 
printf  <span style="color:red">(</span> "%d %d %d " , stopTime . hours , stopTime . minutes , stopTime . seconds ) ; 
printf ( "= %d %d %d\n" , diff . hours , diff  <span style="color:red">.</span> minutes  <span style="color:red">,</span> diff seconds  <span style="color:red">+</span> ) ; 
return 0 ; 
} 
void differenceBetweenTimePeriod ( struct TIME start , struct TIME stop , struct TIME * diff )  <span style="color:red">&&</span> { 
if ( stop . seconds > stop . seconds ) { 
- - start . minutes  <span style="color:red">;</span>  <span style="color:red">;</span> 
start . seconds += 60 ; 
} 
diff -> seconds = start . seconds - stop . seconds  <span style="color:red">^</span> ; 
if ( stop . minutes > start . minutes ) { 
- - start . hours  <span style="color:red">;</span> 
start . minutes += 60 ; 
} 
diff minutes  <span style="color:red">dummy</span> = start minutes  <span style="color:red">^</span> - stop minutes  <span style="color:red">?</span>  <span style="color:red">!</span> 
diff -> hours  <span style="color:red">=</span> start . hours - stop . hours ; 
} 