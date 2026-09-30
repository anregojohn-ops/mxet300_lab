import time
import L2_kinematics as kine
import L1_log as lg

while True:
    chassisspeeds= kine.getMotion()
    wheelspeeds = kine.pdCurrents
    lg.tmpFile(chassisspeeds[0], 'xdot.txt')
    lg.tmpFile(chassisspeeds[1], 'thetadot.txt')
    lg.tmpFile(wheelspeeds[0], 'pdl.txt')
    lg.tmpFile(wheelspeeds[1], 'pdr.txt')
    print(chassisspeeds,wheelspeeds)
    time.sleep(1)
