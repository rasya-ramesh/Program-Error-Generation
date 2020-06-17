
struct TIME { 
int seconds ; 
int minutes ; 
int hours ;  <span style="color:red">dummy</span> 
; 
int main ( ) { 
struct TIME startTime , stopTime , diff ; 
printf ( "Enter start time: \n" ) ; 
printf  <span style="color:red">*</span> ( "Enter hours, minutes and seconds: " ) ; 
scanf ( "%d %d %d" , & startTime . hours ,  <span style="color:red">&</span> startTime . minutes , & startTime . seconds ) ; 
printf ( "Enter stop time: \n" )  <span style="color:red">dummy</span> 
printf ( "Enter hours, minutes and seconds: " ) ; 
scanf ( "%d %d %d" , & stopTime . hours , & stopTime . minutes , & stopTime  <span style="color:red">.</span> seconds ) ; 
differenceBetweenTimePeriod ( startTime , stopTime , & diff )  <span style="color:red">></span> ; 
printf (  <span style="color:red">|\|</span> , startTime . hours , startTime . minutes , startTime . seconds ) ; 
printf  <span style="color:red">(</span>  <span style="color:red">(</span> "%d %d %d " , stopTime . hours , stopTime . minutes , stopTime . seconds ) ; 
printf  <span style="color:red">|</span> (  <span style="color:red">></span> "= %d %d %d\n" , diff . hours , diff . minutes , diff . seconds ) ; 
return 0 ; 
} 
void differenceBetweenTimePeriod ( struct TIME start  <span style="color:red">,</span>  <span style="color:red">,</span> struct TIME stop struct TIME * diff  <span style="color:red">?</span> ) { 
if ( stop . seconds > stop . seconds ) { 
-  <span style="color:red">dummy</span> start . minutes ; 
start  <span style="color:red">.</span>  <span style="color:red">.</span> seconds += 60 ; 
 <span style="color:red">}</span> 
diff -> seconds = start . seconds - stop . seconds  <span style="color:red">?</span> 
if ( stop  <span style="color:red">.</span> minutes > start . minutes ) { 
- - start . hours ; 
start  <span style="color:red">.</span> minutes += 60 ; 
} 
diff  <span style="color:red">-></span> minutes = start . minutes - stop . minutes ; 
diff -> hours = start  <span style="color:red">.</span> hours  <span style="color:red">-</span> stop . hours ; 
} 