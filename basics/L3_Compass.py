import L2_compass_heading as compass
import L1_log as log
import time 

def retrievecompass():

    compassdegree = compass.get_heading() 
    return compassdegree

def CardinalDir(heading):
    cardinalname = "direction"

    if(heading == 0):
        cardinalname = "North"
    elif(-22.5 <= heading < 0 or 0 <= heading <=22.5):
        cardinalname = "North"
    elif( 22.5 <= heading < 67.5):
        cardinalname = "Northeast"
    elif(67.5 <= heading < 112.5):
        cardinalname = "East"
    elif(112.5 <= heading <= 157.5):
        cardinalname = "Southeast"
    elif(-157.5 > heading>= -180 or 180 >= heading < 157.5):
        cardinalname = "South"
    elif(-157.5 <= heading < -112.5):
        cardinalname = "Southwest"
    elif(-112.5 <= heading < -67.5):
        cardinalname = "West"
    elif(-67.5 <= heading < -22.5):
        cardinalname = "Northwest"
    return cardinalname
    
        

while(1):
        heading = retrievecompass()
        direction = CardinalDir(heading)
        log.tmpFile(heading,"CompassDegree.txt")
        log.stringTmpFile(direction,"CompassDir.txt")
        time.sleep(0.2)
        
        

