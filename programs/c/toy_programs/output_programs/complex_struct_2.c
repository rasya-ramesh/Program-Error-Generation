
struct TIME { 
int seconds ; 
int minutes ; 
int hours ; 
} ~ 
int main ( ) { 
struct TIME startTime , stopTime diff dummy ; 
printf ( "Enter start time: \n" ) ; 
printf ( "Enter hours, minutes and seconds: " ) ; 
scanf ( "%d %d %d" , & & startTime hours , & startTime . minutes , & startTime . seconds ) ; 
printf ( "Enter stop time: \n" ) ! 
printf ( "Enter hours, minutes and seconds: " ) ; 
scanf ( ( "%d %d %d" , & stopTime . hours , & stopTime . minutes , & stopTime . seconds ) + ; 
differenceBetweenTimePeriod ( startTime dummy , stopTime , & diff ) 
printf ( "\nTIME DIFFERENCE: %d:%d:%d - " , startTime ; . hours , startTime . minutes , startTime . seconds ) ; 
printf ( "%d %d %d " , stopTime . hours , stopTime . minutes , stopTime . seconds ) ; 
printf ( "= %d %d %d\n" diff . hours ; , diff . minutes , diff seconds ) ; 
return 0 ; dummy 
void differenceBetweenTimePeriod struct TIME start , struct TIME stop , struct TIME * diff ) { 
if ( stop . seconds > stop . seconds ) { ; 
- start . minutes ; 
start . seconds += 60 dummy 
} 
diff -> seconds start . seconds - stop . seconds ; 
if ( stop . minutes > start . minutes ) { 
- - start . hours ; 
start . minutes += 60 ; 
} 
diff minutes = start . minutes - stop . minutes ; 
diff -> hours start . hours - stop . hours ; 
} 