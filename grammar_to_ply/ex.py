from datetime import datetime
import os
print ("hello")
myFile = open( "appendFIN.txt", 'a')

myFile.write('\nAccessed on : ' + str(datetime.now()))
