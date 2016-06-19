from Sensor import *
from Relay import *
import webhelper
import threading


class MotionSensor(Sensor):

    def __init__(self, pin):
        Sensor.__init__(self, pin)
        self.lastMotionTime = 0

    def onStateChange(self, channel):
        print("%s: pin: %d state: %d" % (time.asctime(), channel, self.getState()))
        current_time = time.time()
        time_span = current_time - self.lastMotionTime
        if time_span > 3:
            print("%f report. time span : %d s" % (current_time, time_span))
            threading.Thread(target=report_to_server, args=[current_time]).start()
            self.lastMotionTime = current_time
            relay.switch(0, 1)


def report_to_server(motion_time):
    result = webhelper.report_motion(motion_time)
    print("%f report status: %s" % (motion_time, result))
    relay.switch(0, 0)


def main():
    print("Start motion sensor")
    sensor = MotionSensor(17)
    sensor.setEvent(GPIO.BOTH)
    while True:
        time.sleep(1)

if __name__ == "__main__":
    relay = Relay()
    main()
