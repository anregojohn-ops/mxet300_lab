import L1_ina as vol
import L1_log as log
import time 

while(1):
    batvolt = vol.readVolts()
    log.tmpFile(batvolt,"VoltageData.txt")
    time.sleep(0.2)
    