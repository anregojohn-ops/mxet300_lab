import L1_log as log
import L1_lidar as lidar
import L2_vector as vec
from time import sleep
sensor = lidar.Lidar()
sensor.connect()
sensor.run()
sleep(2) # let the first scan arrive
while True:
# get a scan from the sensor
    lidardata = sensor.get()
# find the nearest obstacle in that scan
    near = vec.getNearest(lidardata)
# write the distance to its own file
    log.tmpFile(near[0],"distance.txt")

# write the angle to its own file
    log.tmpFile(near[1],"angle.txt")

    xycomp = vec.polar2cart(near[0],near[1])

    log.tmpFile(xycomp[0], "xcomp.txt")
    log.tmpFile(xycomp[1], "ycomp.txt")


# sleep
    sleep(0.1)